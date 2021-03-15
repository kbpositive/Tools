class Graph:
    def __init__(self):
        self.vertices = {}
        self.matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = len(self.vertices)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0 for row in range(len(self.matrix)+1)])

    def add_edge(self, edge):
        self.add_vertex(edge[0])
        self.add_vertex(edge[1])
        row = self.vertices[edge[0]]
        col = self.vertices[edge[1]]
        self.matrix[row][col] = -edge[2]
        self.matrix[col][row] = edge[2]

    def print_graph(self):
        print("",end="\t")
        for vertex in self.vertices:
            print(str(vertex),end="\t")
        print("")
        for row in self.vertices:
            print(str(row),end="\t")
            for col in self.vertices:
                print(self.matrix[self.vertices[row]][self.vertices[col]],end="\t")
            print("")

    @property
    def m(self):
        return len([x for y in [j[i:] for i,j in enumerate(self.matrix)] for x in y if x != 0])

    @property
    def n(self):
        return len(self.vertices)


if __name__ == '__main__':
    G = Graph()
    for edge in [[1,2,4],[1,3,3],[1,4,2],[2,3,7],[4,3,2],[3,5,9],[4,5,5]]:
        G.add_edge(edge)
    G.matrix
    G.add_edge([3,6,1])
    G.add_edge([3,7,8])
    G.add_edge([4,6,2])
    G.add_edge([4,7,6])
    G.add_edge([5,7,3])

    assert G.m == 12
    assert G.n == 7


    G.print_graph()
    print("pass")
