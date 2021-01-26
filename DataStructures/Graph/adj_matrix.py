class Graph:
    def __init__(self, edges):
        self.edges = set(frozenset((a,b,c)) for a,b,c in edges)


    def add_edge(self, a, b):
        return

    def add_vertex(self, v):
        return

    def print_graph():
        return


if __name__ == '__main__':
    G = Graph({(1,2,2),(1,3,2),(1,4,2),(2,3,2),(4,3,2),(3,5,2),(4,5,2)})

    print("pass")
