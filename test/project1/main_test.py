# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest

from project1.main import (
    make_complete_graph,
    compute_in_degrees,
    in_degree_distribution,
    EX_GRAPH0,
    EX_GRAPH1,
    EX_GRAPH2,
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
            compute_in_degrees(EX_GRAPH0),
            {0: 2, 1: 0, 2: 0}
        )
        self.assertDictEqual(
            compute_in_degrees(EX_GRAPH1),
            {0: 3, 1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0}
        )
        self.assertDictEqual(
            compute_in_degrees(EX_GRAPH2),
            {0: 3, 1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 0, 7: 1, 8: 2, 9: 6}
        )


class TestInDegreeDistribution(unittest.TestCase):

    def test_empty_graph(self):
        self.assertDictEqual(in_degree_distribution({}), {})

    def test_one_node_graph(self):
        self.assertDictEqual(in_degree_distribution({0: set()}), {0: 1})

    def test_in_degree_distribution_returns_correct_result(self):
        self.assertDictEqual(
            in_degree_distribution(EX_GRAPH0),
            {0: 2, 2: 1}
        )
        self.assertDictEqual(
            in_degree_distribution(EX_GRAPH1),
            {1: 4, 0: 1, 2: 1, 3: 1}
        )
        self.assertDictEqual(
            in_degree_distribution(EX_GRAPH2),
            {0: 1, 1: 4, 2: 3, 3: 1, 6: 1}
        )
