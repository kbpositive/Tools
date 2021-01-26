class Graph:
    def __init__(self, edges):
        self.edges = set(frozenset((a,b)) for a,b in edges)
        self.vertices = {}
        for a,b in self.edges:
            self.addEdge(a,b)
        for vertex in self.vertices:
            self.add_vertex(vertex)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def addEdge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        self.edges.add(frozenset([a,b]))
        self.vertices[a][b] = self.vertices[b]
        self.vertices[b][a] = self.vertices[a]

    def removeVertex(self, item):
        for vertex, neighbor in self.vertices.items():
            if item in neighbor:
                del neighbor[item]
                self.edges.remove(frozenset([vertex,item]))
        del self.vertices[item]

    def removeEdge(self, a, b):
        edge = frozenset([a,b])
        if edge in self.edges:
            self.edges.remove(edge)
            del self.vertices[a][b]
            del self.vertices[b][a]

    @property
    def m(self):
        return len(self.edges)

    @property
    def n(self):
        return len(self.vertices)

if __name__ == '__main__':
    G = Graph({(1,2),(1,3),(1,4),(2,3),(4,3),(3,5),(4,5)})

    def print_graph(graph):
        for vertex,neighbors in graph.items():
            print(str(vertex) + " :", end=" ")
            for neighbor in neighbors:
                print(str(neighbor), end=" ")
            print("")



    #print_graph(G.vertices)

    assert G.m == 7
    assert G.n == 5

    G.removeEdge(2,3)
    assert G.m == 6
    assert G.n == 5

    G.removeEdge(1,4)
    assert G.m == 5
    assert G.n == 5

    G.addEdge(2,3)
    assert G.m == 6
    assert G.n == 5

    G.addEdge(3,9)
    assert G.m == 7
    assert G.n == 6

    G.removeVertex(3)
    assert G.m == 2
    assert G.n == 5

    G.addEdge(3,9)
    assert G.m == 3
    assert G.n == 6

    G.addEdge(1,3)
    assert G.m == 4
    assert G.n == 6

    G.addEdge(5,3)
    assert G.m == 5
    assert G.n == 6

    G.add_vertex(9)
    assert G.m == 5
    assert G.n == 6

    #print_graph(G.vertices)

    assert list(G.vertices[5][4][5][3][1][2][1][3][9].keys())[0] == 3

    print('Pass')
