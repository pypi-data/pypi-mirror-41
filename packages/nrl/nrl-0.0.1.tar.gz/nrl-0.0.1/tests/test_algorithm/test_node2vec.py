# -*- coding: utf-8 -*-

"""Tests for Node2Vec."""

import unittest

import networkx as nx
from gensim.models import Word2Vec
from node2vec import Node2Vec

from nrl.model import Node2VecModel
from nrl.model.word2vec import Word2VecParameters
from nrl.walker import RandomWalkParameters
from tests.constants import WEIGHTED_NETWORK_PATH, get_test_network


class TestNode2Vec(unittest.TestCase):
    """Test case for DeepWalk."""

    # TODO: test using a directed graph

    def test_node2vec_unweighted(self):
        """Test Node2Vec."""
        graph = get_test_network()
        random_walk_parameters = RandomWalkParameters(
            number_paths=5,
            max_path_length=10,
            is_weighted=False
        )
        word2vec_parameters = Word2VecParameters()

        nrl_n2v = Node2VecModel(graph, random_walk_parameters, word2vec_parameters)
        word2vec = nrl_n2v.fit()

        self.assertIsInstance(word2vec, Word2Vec)

    def test_node2vec_weighted(self):
        """Test Node2Vec."""
        graph = get_test_network(path=WEIGHTED_NETWORK_PATH)
        random_walk_parameters = RandomWalkParameters(
            number_paths=5,
            max_path_length=10,
        )
        word2vec_parameters = Word2VecParameters()

        nrl_n2v = Node2VecModel(graph, random_walk_parameters, word2vec_parameters)
        word2vec = nrl_n2v.fit()

        self.assertIsInstance(word2vec, Word2Vec)

    def test_precompute_probs(self):
        """Test the pre-compute_probs function."""
        g1 = nx.read_weighted_edgelist(path=WEIGHTED_NETWORK_PATH, nodetype=int)

        n1 = Node2Vec(g1)
        d1 = n1._precompute_probabilities()

        g2 = get_test_network(WEIGHTED_NETWORK_PATH)
        random_walk_parameters = RandomWalkParameters(
            number_paths=5,
            max_path_length=10,
        )
        word2vec_parameters = Word2VecParameters()

        n2 = Node2VecModel(g2, random_walk_parameters, word2vec_parameters)

        for key in d1.keys():
            vertex1 = d1[key]
            vertex2 = n2.graph.vs.find(name=str(key))
            self.assertListEqual(
                sorted(vertex1['neighbors']),
                sorted([int(nbr['name']) for nbr in vertex2.neighbors()])
            )
            self.assertListEqual(
                list(vertex1['first_travel_key']),
                list(vertex2['first_travel_key']))
            for inner_key in vertex1['probabilities'].keys():
                self.assertListEqual(
                    list(vertex1['probabilities'][inner_key]),
                    list(vertex2['probabilities'][str(inner_key)])
                )
