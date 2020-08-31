class DisjointSet:
    def __init__(self, graph: dict):
        self.graph = graph

    def count(self, nodes: int) -> int:
        return [row[0] for row in list(self.graph.values())].count(nodes)

    def find(self, node: str) -> int:
        root = self.graph[node][1]
        while root != self.graph[root][1]:
            root = self.graph[root][1]
        return root

    def union(self, pair: list):
        root_a = self.find(pair[0])
        root_b = self.find(pair[1])
        if root_a != root_b:
            if self.count(self.graph[root_a][0]) <= self.count(self.graph[root_b][0]):
                self.graph[root_b] = self.graph[root_a]
                self.graph[pair[1]] = self.graph[root_a]  # path compression
            else:
                self.graph[root_a] = self.graph[root_b]
                self.graph[pair[0]] = self.graph[root_b]  # path compression
