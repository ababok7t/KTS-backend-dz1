from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        visited_nodes = []
        self._dfs_helper(self._root, visited_nodes)
        return visited_nodes

    def _dfs_helper(self, node: Node, visited_nodes: list[Node]) -> None:
        if node not in visited_nodes:
            visited_nodes.append(node)
            for neighbor in node.outbound:
                self._dfs_helper(neighbor, visited_nodes)

    def bfs(self) -> list[Node]:
        visited_nodes = []
        queue = [self._root]

        while queue:
            current_node = queue.pop(0)
            if current_node not in visited_nodes:
                visited_nodes.append(current_node)
                for neighbor in current_node.outbound:
                    queue.append(neighbor)

        return visited_nodes

    def reset_visited(self):
        queue = [self._root]
        while queue:
            current_node = queue.pop(0)
            current_node.visited = False
            for neighbor in current_node.neighbors:
                queue.append(neighbor)
