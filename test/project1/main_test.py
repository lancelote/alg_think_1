# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest

from project1.main import (
    make_complete_graph,
    compute_in_degrees,
    in_degree_distribution,
)
from project1.alg_module1_graphs import (
    GRAPH0, GRAPH1, GRAPH2, GRAPH3, GRAPH4, GRAPH5, GRAPH6, GRAPH7, GRAPH8,
    GRAPH9
)


class TestMakeCompleteGraph(unittest.TestCase):

    def test_empty_graph(self):
        self.assertDictEqual(make_complete_graph(0), {})

    def test_one_node_graph(self):
        self.assertDictEqual(make_complete_graph(1), {0: set()})

    def test_make_complete_graph_returns_correct_result(self):
        self.assertDictEqual(
            make_complete_graph(3),
            {0: {1, 2}, 1: {0, 2}, 2: {0, 1}})


class TestComputeInDegrees(unittest.TestCase):

    def test_empty_graph(self):
        self.assertDictEqual(compute_in_degrees({}), {})

    def test_one_node_graph(self):
        self.assertDictEqual(compute_in_degrees({0: set()}), {0: 0})

    def test_compute_in_degrees_returns_correct_result(self):
        self.assertDictEqual(
            compute_in_degrees(GRAPH0),
            {0: 1, 1: 1, 2: 1, 3: 1}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH1),
            {0: 4, 1: 0, 2: 0, 3: 0, 4: 0}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH2),
            {0: 0, 1: 1, 2: 1, 3: 1, 4: 1}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH3),
            {0: 4, 1: 4, 2: 4, 3: 4, 4: 4}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH4),
            {"dog": 1, "cat": 1, "monkey": 0, "banana": 1}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH5),
            {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH6),
            {1: 2, 2: 2, 3: 1, 4: 3, 5: 2, 6: 2, 7: 2, 9: 2}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH7),
            {0: 10, 1: 9, 2: 11, 3: 9, 4: 12, 5: 0, 6: 0, 7: 2, 8: 0, 9: 0,
             10: 1, 11: 0, 12: 0, 13: 1, 14: 0}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH8),
            {0: 16, 1: 11, 2: 5, 3: 3, 4: 2, 5: 1, 6: 1, 7: 2, 8: 2, 9: 0,
             10: 0, 11: 0, 12: 0, 13: 0, 14: 1, 15: 0, 16: 0, 17: 1, 18: 0,
             19: 0}
        )
        self.assertDictEqual(
            compute_in_degrees(GRAPH9),
            {0: 27, 1: 32, 2: 36, 3: 17, 4: 34, 5: 33, 6: 32, 7: 3, 8: 3, 9: 3,
             10: 2, 11: 2, 12: 1, 13: 2, 14: 2, 15: 4, 16: 3, 17: 1, 18: 2,
             19: 0, 20: 4, 21: 2, 22: 4, 23: 0, 24: 3, 25: 0, 26: 1, 27: 1,
             28: 2, 29: 2, 30: 0, 31: 0, 32: 1, 33: 0, 34: 0, 35: 0, 36: 0,
             37: 1, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0,
             46: 0, 47: 0, 48: 0, 49: 0}
        )


class TestInDegreeDistribution(unittest.TestCase):

    def test_empty_graph(self):
        self.assertDictEqual(in_degree_distribution({}), {})

    def test_one_node_graph(self):
        self.assertDictEqual(in_degree_distribution({0: set()}), {0: 1})

    def test_in_degree_distribution_returns_correct_result(self):
        self.assertDictEqual(
            in_degree_distribution(GRAPH0),
            {1: 4}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH1),
            {0: 4, 4: 1}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH2),
            {0: 1, 1: 4}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH3),
            {4: 5}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH4),
            {0: 1, 1: 3}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH5),
            {1: 2, 2: 2, 3: 2, 4: 2}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH6),
            {1: 1, 2: 6, 3: 1}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH7),
            {0: 7, 1: 2, 2: 1, 9: 2, 10: 1, 11: 1, 12: 1}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH8),
            {16: 1, 1: 4, 2: 3, 3: 1, 5: 1, 0: 9, 11: 1}
        )
        self.assertDictEqual(
            in_degree_distribution(GRAPH9),
            {32: 2, 17: 1, 34: 1, 3: 5, 36: 1, 1: 6, 0: 21, 33: 1, 4: 3, 27: 1,
             2: 8}
        )
