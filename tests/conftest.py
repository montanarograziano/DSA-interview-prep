"""Fixtures for tests."""

import pytest

from src.graphs import GraphNode


@pytest.fixture
def graph1() -> GraphNode:
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node6 = GraphNode(6)
    node7 = GraphNode(7)

    node1.neighbors = [node2, node3]
    node2.neighbors = [node4, node5]
    node3.neighbors = [node6, node7]

    return node1


@pytest.fixture
def graph2() -> GraphNode:
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node6 = GraphNode(6)
    node7 = GraphNode(7)
    node8 = GraphNode(8)
    node9 = GraphNode(9)
    node10 = GraphNode(10)

    node1.neighbors = [node2, node3]
    node2.neighbors = [node4, node5]
    node3.neighbors = [node6, node7]
    node4.neighbors = [node8]
    node5.neighbors = [node9]
    node6.neighbors = [node10]

    return node1


@pytest.fixture
def edges():
    return {
        (1, 2): 1,
        (1, 3): 1,
        (2, 4): 3,
        (2, 5): 10,
        (3, 6): 1,
        (3, 7): 3,
    }
