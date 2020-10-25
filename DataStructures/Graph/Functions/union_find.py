def find_root(graph, node):
	root = node
	hist = []
	while root not in list(graph[root].keys()):
		root = list(graph[root].keys())[0]
		if root in hist:
			return hist
		hist.append(root)
	return [root]


def count(graph, value) -> int:
	temp_a = list(graph.values())
	temp_b = [y for x in temp_a for y in list(x.values())]
	return temp_b.count(value)


def union(graph, pair):
	root_a = find_root(graph, pair[0])
	root_b = find_root(graph, pair[1])
	if set(sorted(root_a[0])) != set(sorted(root_b[0])):
		if count(graph, graph[root_a[0]]) <= count(graph, graph[root_b[0]]):
			graph[root_b[0]] = graph[root_a[0]]
			graph[pair[1]] = graph[root_a[0]]  # path compression
		else:
			graph[root_a[0]] = graph[root_b[0]]
			graph[pair[0]] = graph[root_b[0]]  # path compression

from DataStructures.Graph import directed_acyclic, disjoint_set

c = disjoint_set.Graph(10)
print(c.graph)

print(find_root(c.graph, 1))
print(count(c.graph, 1))
print(find_root(c.graph, 4))
print(count(c.graph, 4))

union(c.graph, (1, 4))
print(c.graph)

print(find_root(c.graph, 1))
print(count(c.graph, 1))
print(find_root(c.graph, 4))
print(count(c.graph, 4))
