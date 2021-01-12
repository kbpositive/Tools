class Graph:
    def __init__(self, vertices, edges):
        self.edges = set(frozenset((a,b)) for a,b in edges)
        self.neighbors = {}
        for vertex in vertices:
            self.addVertex(vertex)
        for a,b in self.edges:
            self.addEdge(a,b)

    def addVertex(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors[vertex] = set()

    def addEdge(self, a, b):
        self.addVertex(a)
        self.addVertex(b)
        self.edges.add(frozenset([a,b]))
        self.neighbors[a].add(b)
        self.neighbors[b].add(a)

    def removeVertex(self, vertex):
        neighborList = list(self.neighbors[vertex])
        for neighbor in neighborList:
            self.removeEdge(vertex, neighbor)
        del self.neighbors[vertex]

    def removeEdge(self, a, b):
        edge = frozenset([a,b])
        if edge in self.edges:
            self.edges.remove(edge)
            self.neighbors[a].remove(b)
            self.neighbors[b].remove(a)

    def getNeighbors(self, vertex):
        return set(self.neighbors[vertex])

    @property
    def m(self):
        return len(self.edges)

    @property
    def n(self):
        return len(self.neighbors)

if __name__ == '__main__':
    G = Graph(
        [1,1,2,3,7,6,6,4,8,5],
        {(1,2),(2,3),(6,7),(2,3),(8,3),(2,6),(8,4),(5,1)})

    assert G.getNeighbors(3) == {8,2}
    assert G.m == 7
    assert G.n == 8

    G.removeEdge(2,3)
    assert G.m == 6
    assert G.n == 8

    G.removeEdge(2,3)
    assert G.m == 6
    assert G.n == 8

    G.addEdge(2,3)
    assert G.m == 7
    assert G.n == 8

    G.removeVertex(3)
    assert G.m == 5
    assert G.n == 7

    G.addVertex(9)
    assert G.m == 5
    assert G.n == 8

    print('Pass')
