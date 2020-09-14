from DataStructures.Graph import disjoint_set
from Algorithms import kruskals_mst


g = disjoint_set.DisjointSet(5)
g.graph = kruskals_mst.union_find(g.graph, [[g.graph[0][0], g.graph[1][0]]])
print(g.graph)
