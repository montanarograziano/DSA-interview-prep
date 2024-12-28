"""Test for Graphs algorithms."""

import pytest

from src.graphs import GraphNode, dijkstra, shortest_path


def test_shortest_path(graph1: GraphNode, graph2: GraphNode):
    assert shortest_path(graph1, graph1.neighbors[1]) == [1, 3]
    assert shortest_path(graph1, graph1.neighbors[0]) == [1, 2]
    assert shortest_path(graph1, graph1.neighbors[1].neighbors[0]) == [1, 3, 6]
    assert shortest_path(graph1, graph1.neighbors[1].neighbors[1]) == [1, 3, 7]
    assert shortest_path(graph2, graph2.neighbors[1]) == [1, 3]
    assert shortest_path(graph2, graph2.neighbors[0]) == [1, 2]
    assert shortest_path(graph2, graph2.neighbors[1].neighbors[0]) == [1, 3, 6]
    assert shortest_path(graph2, graph2.neighbors[1].neighbors[1]) == [1, 3, 7]
    assert shortest_path(graph2, graph2.neighbors[0].neighbors[0]) == [1, 2, 4]
    assert shortest_path(graph2, graph2.neighbors[0].neighbors[1]) == [1, 2, 5]


def test_dijkstra(
    graph1: GraphNode, graph2: GraphNode, edges: dict[tuple[int, int], int]
):
    assert dijkstra(edges, graph1, graph1.neighbors[1]) == [1, 3]
    assert dijkstra(edges, graph1, graph1.neighbors[0]) == [1, 2]
    assert dijkstra(edges, graph1, graph1.neighbors[1].neighbors[0]) == [1, 3, 6]
    assert dijkstra(edges, graph1, graph1.neighbors[1].neighbors[1]) == [1, 3, 7]
    assert dijkstra(edges, graph2, graph2.neighbors[1]) == [1, 3]


if __name__ == "__main__":
    pytest.main()
