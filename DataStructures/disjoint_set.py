class DisjointSet:
    def __init__(self, graph: dict):
        self.graph = graph

    def count(self, value: int) -> int:
        return [row[1] for row in list(self.graph.values())].count(value)

    def find(self, node):
        root = self.graph[node][0]
        while root != self.graph[root][0]:
            root = self.graph[root][0]
        return root

    def union(self, pair):
        root_a = self.find(pair[0])
        root_b = self.find(pair[1])
        if root_a != root_b:
            if self.count(self.graph[root_a][1]) <= self.count(self.graph[root_b][1]):
                self.graph[root_b] = self.graph[root_a]
                self.graph[pair[1]] = self.graph[root_a]  # path compression
            else:
                self.graph[root_a] = self.graph[root_b]
                self.graph[pair[0]] = self.graph[root_b]  # path compression
