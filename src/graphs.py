"""Implementations of common algorithms for Graphs."""

import heapq
from collections import deque
from typing import Optional

from typing_extensions import Self


class GraphNode:
    def __init__(self, val: int = 0, neighbors: Optional[list[Self]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Graph:
    def __init__(self, nodes: Optional[list[GraphNode]] = None):
        self.nodes = nodes if nodes is not None else []


class Edge:
    def __init__(self, _from: GraphNode, _to: GraphNode, _weight: int = 0):
        self._from = _from
        self._to = _to
        self._weight = _weight


def shortest_path(start: GraphNode, end: GraphNode) -> list[int]:
    """Shortest Path implementation. The function finds the shortest path between two nodes in a graph.

    Args:
        start (GraphNode): Starting node for the path.
        end (GraphNode): Ending node for the path.

    Returns:
        list[int]: Shortest path between the start and end nodes.
    """

    queue = deque([(start, [start.val])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in node.neighbors:
            queue.append((neighbor, path + [neighbor.val]))

    return []


def dijkstra(
    edges: dict[tuple[int, int], int], start: GraphNode, end: GraphNode
) -> list[int]:
    """Dijkstra's algorithm implementation. The function finds the shortest path between two nodes in a weighted graph.

    Args:
        edges dict[tuple[int, int], int]: Dict of edges in the graph.
            Keys are pairs (from, to)  and values are weights.
        start (GraphNode): Starting node for the path.
        end (GraphNode): Ending node for the path.

    Returns:
        list[int]: Shortest path between the start and end nodes.
    """

    queue = [(0, [start.val], start)]
    heapq.heapify(queue)
    visited = set()

    while queue:
        weight, path, node = heapq.heappop(queue)

        if node == end:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in node.neighbors:
            heapq.heappush(
                queue,
                (
                    weight + edges[(node.val, neighbor.val)],
                    path + [neighbor.val],
                    neighbor,
                ),
            )

    return []
