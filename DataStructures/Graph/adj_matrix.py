class Graph:
    def __init__(self, edges):
        self.edges = []
        self.vertices = {}
        self.matrix = []
        for edge in edges:
            self.add_edge(edge)
        for vertex in self.vertices:
            self.add_vertex(vertex)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = len(self.vertices)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0 for row in range(len(self.matrix)+1)])

    def add_edge(self, edge):
        self.add_vertex(edge[0])
        self.add_vertex(edge[1])
        self.edges.append(edge)
        row = self.vertices[edge[0]]
        col = self.vertices[edge[1]]
        self.matrix[row][col] = edge[2]
        self.matrix[col][row] = -edge[2]

    @property
    def m(self):
        return len(self.edges)

    @property
    def n(self):
        return len(self.vertices)


if __name__ == '__main__':
    G = Graph([[1,2,4],[1,3,3],[1,4,2],[2,3,7],[4,3,2],[3,5,9],[4,5,5]])

    G.add_edge([3,6,1])
    G.add_edge([3,7,8])
    G.add_edge([4,6,2])
    G.add_edge([4,7,6])
    G.add_edge([5,7,3])

    assert G.m == 12
    assert G.n == 7
    def print_graph(graph):
        print("",end="\t")
        for vertex in graph.vertices:
            print(str(vertex),end="\t")
        print("")
        for row in graph.vertices:
            print(str(row),end="\t")
            for col in graph.vertices:
                print(graph.matrix[graph.vertices[row]][graph.vertices[col]],end="\t")
            print("")

    print_graph(G)
    print("pass")
