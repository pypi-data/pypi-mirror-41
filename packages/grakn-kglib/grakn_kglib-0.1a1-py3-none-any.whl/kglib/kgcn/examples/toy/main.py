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

import grakn
import numpy as np
import tensorflow as tf

import kglib.kgcn.models.model as model
import kglib.kgcn.neighbourhood.data.sampling.ordered as ordered
import kglib.kgcn.neighbourhood.data.sampling.sampler as samp
import kgcn.neighbourhood.schema.strategy as schema_strat

flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_boolean('debug', False, 'Enable debugging')
flags.DEFINE_float('learning_rate', 0.05, 'Learning rate')
flags.DEFINE_integer('classes_length', 3, 'Number of classes')
flags.DEFINE_integer('features_length', 192, 'Number of features after encoding')
flags.DEFINE_integer('starting_concepts_features_length', 4,  ## 143,
                     'Number of features after encoding for the nodes of interest, which excludes the features for '
                     'role_type and role_direction')
flags.DEFINE_integer('aggregated_length', 4, 'Length of aggregated representation of neighbours, a hidden dimension')
flags.DEFINE_integer('output_length', 4, 'Length of the output of "combine" operation, taking place at each depth, '
                                          'and the final length of the embeddings')

flags.DEFINE_integer('max_training_steps', 2500, 'Max number of gradient steps to take during gradient descent')

TIMESTAMP = time.strftime("%Y-%m-%d_%H-%M-%S")
flags.DEFINE_string('log_dir', './out/out_' + TIMESTAMP, 'directory to use to store data from training')


def main():
    keyspace = 'toy'
    uri = "localhost:48555"

    client = grakn.Grakn(uri=uri)
    train_session = client.session(keyspace=keyspace)
    tx = train_session.transaction(grakn.TxType.WRITE)

    label_types = ['A', 'B', 'C']

    concepts = []
    labels = []

    for label_type in label_types:

        target_concept_query = f"match $x($label) isa example; $label isa {label_type}; get;"

        answers = tx.query(target_concept_query)
        new_concepts = [ans.get('x') for ans in answers]

        base_label = [0, 0, 0]
        base_label[label_types.index(label_type)] = 1

        concepts += new_concepts
        labels += [base_label for _ in new_concepts]

    labels = np.array(labels, dtype=np.float32)

    neighbour_sample_sizes = (1,)

    sampling_method = ordered.ordered_sample

    samplers = []
    for sample_size in neighbour_sample_sizes:
        samplers.append(samp.Sampler(sample_size, sampling_method, limit=sample_size + 1))

    # Strategies
    role_schema_strategy = schema_strat.SchemaRoleTraversalStrategy(include_implicit=False, include_metatypes=False)
    thing_schema_strategy = schema_strat.SchemaThingTraversalStrategy(include_implicit=False, include_metatypes=False)

    traversal_strategies = {'role': role_schema_strategy,
                            'thing': thing_schema_strategy}

    kgcn = model.KGCN(tx, traversal_strategies, samplers, features_to_exclude=['neighbour_data_type',
                                                                               'neighbour_value_long',
                                                                               'neighbour_value_double',
                                                                               'neighbour_value_boolean',
                                                                               'neighbour_value_date',
                                                                               'neighbour_value_string'])

    kgcn.train(tx, concepts, labels)
    kgcn.evaluate(tx, concepts, labels)
    # kgcn.predict(tx, concepts)


if __name__ == "__main__":
    main()
