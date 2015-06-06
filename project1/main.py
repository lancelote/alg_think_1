"""
Algorithmic Thinking Project 1
"""

from collections import Counter

# Test data
# Adjacency lists
EX_GRAPH0 = {0: {1, 2},
             1: {},
             2: {}}
EX_GRAPH1 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3},
             3: {0},
             4: {1},
             5: {2},
             6: {}}
EX_GRAPH2 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3, 7},
             3: {7},
             4: {1},
             5: {2},
             6: {},
             7: {3},
             8: {1, 2},
             9: {0, 3, 4, 5, 6, 7}}


# Project implementation
def make_complete_graph(num_nodes):
    """
    Makes a dictionary representation of complete directed graph with given
    number of nodes

    :param num_nodes: number of nodes in the graph
    :return: a dictionary corresponding to a complete directed graph
    """
    nodes = set(range(num_nodes))
    return {n: nodes - {n} for n in range(num_nodes)}


def compute_in_degrees(digraph):
    """
    Compute in-degree of every node of a given graph

    :param digraph: a dictionary corresponding to a directed graph
    :return: a dictionary {node: in-degree}
    """
    return {k: len(v) for (k, v) in digraph.items()}


def in_degree_distribution(digraph):
    """
    Compute in-degree distribution of a given graph

    :param digraph: a dictionary corresponding to a directed graph
    :return: a dictionary corresponding to a in-degree distribution of a given
    graph {in-degree: occurence}
    """
    in_degrees = compute_in_degrees(digraph)
    return Counter(in_degrees.values())
