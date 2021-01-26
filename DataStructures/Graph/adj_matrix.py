class Graph:
    def __init__(self, edges):
        self.edges = {}
        for edge in edges:
            self.edges[frozenset(edge[:2])] = edge[2]
        self.vertices = {}
        self.matrix = []
        for edgeSet in self.edges.items():
            self.add_edge((list(edgeSet[0]) + [edgeSet[1]]))
        for vertex in self.vertices:
            self.add_vertex(vertex)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = len(self.vertices)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0 for row in range(len(self.matrix)+1)])

    def add_edge(self, edge):
        edgeData = list(edge)
        self.add_vertex(edgeData[0])
        self.add_vertex(edgeData[1])
        self.edges[frozenset(edgeData[:2])] = edgeData[2]
        row = self.vertices[edgeData[0]]
        col = self.vertices[edgeData[1]]
        self.matrix[row][col] = edgeData[2]
        self.matrix[col][row] = -edgeData[2]

    @property
    def m(self):
        return len(self.edges)

    @property
    def n(self):
        return len(self.vertices)


if __name__ == '__main__':
    G = Graph({(1,2,4),(1,3,3),(1,4,2),(2,3,7),(4,3,2),(3,5,9),(4,5,5)})

    def print_graph(graph):
        print("",end="\t")
        for vertex in graph.vertices:
            p
        for row in graph.vertices:
            for col in graph.vertices:
                print(graph.matrix[graph.vertices[row]][graph.vertices[col]],end="\t")
            print("")
    print_graph(G)
    print("pass")
