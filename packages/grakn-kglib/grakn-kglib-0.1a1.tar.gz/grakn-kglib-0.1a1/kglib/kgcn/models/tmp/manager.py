#
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.
#

import time
import typing as typ

import numpy as np
import tensorflow as tf

import kglib.kgcn.preprocess.persistence
import kglib.kgcn.models.metrics as metrics


def build_array_placeholders(batch_size, neighbourhood_sizes, features_length,
                             feature_types: typ.Union[typ.List[typ.MutableMapping[str, tf.DType]], tf.DType],
                             name=None):
    array_neighbourhood_sizes = list(reversed(neighbourhood_sizes))
    neighbourhood_placeholders = []
    for i in range(len(array_neighbourhood_sizes) + 1):
        shape = [None] + list(array_neighbourhood_sizes[i:]) + [features_length]

        try:
            phs = tf.placeholder(feature_types, shape=shape, name=name)
        except:
            phs = {name: tf.placeholder(type, shape=shape, name=name) for name, type in feature_types[i].items()}

        neighbourhood_placeholders.append(phs)
    return neighbourhood_placeholders


# TODO Update and move now this isn't used here


def build_labels_placeholder(batch_size, num_classes, name=None):
    return tf.placeholder(tf.float32, shape=(batch_size, num_classes), name=name)


class LearningManager:

    def __init__(self, learner, max_training_steps, log_dir, dataset_initializer):
        self._learner = learner
        self._max_training_steps = max_training_steps
        self._log_dir = log_dir
        self._dataset_initializer = dataset_initializer

    def __call__(self, sess, neighbourhoods_input, labels_input):
        self.labels_input = labels_input
        self.train_op, self.loss, self.class_predictions, self.micro_precisions, self.micro_precisions_update, \
        self.micro_recalls, self.micro_recalls_update, self.f1_score, self.update_f1_score, \
        self.confusion_matrix = self._learner.train_and_evaluate(
            neighbourhoods_input, labels_input)

        # Build the summary Tensor based on the TF collection of Summaries.
        self.summary = tf.summary.merge_all()

        # Add the variable initializer Op.
        init_global = tf.global_variables_initializer()
        init_local = tf.local_variables_initializer()  # Added to initialise tf.metrics.recall
        init_tables = tf.tables_initializer()

        # Instantiate a SummaryWriter to output summaries and the Graph.
        self.summary_writer = tf.summary.FileWriter(self._log_dir, sess.graph)

        # Run the Op to initialize the variables.
        sess.run(init_global)
        sess.run(init_local)
        sess.run(init_tables)

    def train(self, sess, feed_dict):
        print("\n\n========= Training and Evaluation =========")
        start_time = time.time()
        for step in range(self._max_training_steps):
            _ = sess.run(self._dataset_initializer, feed_dict=feed_dict)

            if step % int(self._max_training_steps / 20) == 0:

                _, loss_value, micro_precision_values, _, micro_recall_values, _, f1_score_value, _, \
                confusion_matrix_value, class_prediction_values, labels = \
                    sess.run([self.train_op, self.loss, self.micro_precisions, self.micro_precisions_update,
                              self.micro_recalls, self.micro_recalls_update, self.f1_score, self.update_f1_score,
                              self.confusion_matrix, self.class_predictions, self.labels_input])
                print(f'Step {step}    -------------')
                print(f'Loss: {loss_value:.2f}')
                metrics.report_multiclass_metrics(np.argmax(labels, axis=-1),
                                                  np.argmax(class_prediction_values, axis=-1))

                summary_str = sess.run(self.summary, feed_dict=feed_dict)
                self.summary_writer.add_summary(summary_str, step)
                self.summary_writer.flush()
            else:
                _, loss_value = sess.run([self.train_op, self.loss])

        duration = time.time() - start_time
        print(f'Time taken:    {duration:.2f}')
        print("\n\n========= Training and Evaluation Complete =========\n\n")

    def evaluate(self, sess, feed_dict):
        _ = sess.run(self._dataset_initializer, feed_dict=feed_dict)
        micro_precision_values, _, micro_recall_values, _, f1_score_value, _, confusion_matrix_value, \
        class_prediction_values, labels = sess.run(
            [self.micro_precisions, self.micro_precisions_update,
             self.micro_recalls, self.micro_recalls_update, self.f1_score,
             self.update_f1_score, self.confusion_matrix, self.class_predictions, self.labels_input])

        print("\n\n========= Evaluation =========")

        metrics.report_multiclass_metrics(np.argmax(labels, axis=-1),
                                          np.argmax(class_prediction_values, axis=-1))

        print("\n\n========= Evaluation Complete =========")

        print('\n\nClass scores')
        print(class_prediction_values)
        kglib.kgcn.preprocess.persistence.save_variable(class_prediction_values,
                                                        self._log_dir + '/class_scores.p')

        return confusion_matrix_value, class_prediction_values

    # TODO Made predict do the exact same as evaluate to use as test, change back
    def predict(self, sess, feed_dict):
        return self.evaluate(sess, feed_dict)

    # def predict(self, sess, feed_dict):
    #     print("\n\n========= Prediction =========")
    #     class_prediction_values = sess.run([self.class_predictions], feed_dict=feed_dict)
    #     print(f'predictions: \n{class_prediction_values}')
    #     print("\n\n========= Prediction Complete =========\n\n")
