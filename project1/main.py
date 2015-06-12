"""
Algorithmic Thinking Project 1
"""

from collections import Counter

# Do not change set([]) notation, coursera test will fail
EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


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
    nodes = set(digraph.keys())
    return {k: sum(k in digraph[node] for node in nodes - {k})
            for k in digraph.keys()}


def in_degree_distribution(digraph):
    """
    Compute in-degree distribution of a given graph

    :param digraph: a dictionary corresponding to a directed graph
    :return: a dictionary corresponding to a in-degree distribution of a given
    graph {in-degree: occurence}
    """
    in_degrees = compute_in_degrees(digraph)
    return dict(Counter(in_degrees.values()))
