def count(graph: dict, nodes: int) -> int:
    return [row[0] for row in list(graph.values())].count(nodes)


def find(graph: dict, node: str) -> int:
    root = graph[node][1]
    while root != graph[root][1]:
        root = graph[root][1]
    return root


def union(graph: dict, pair: list):
    rootA = find(graph, pair[0])
    rootB = find(graph, pair[1])
    if rootA != rootB:
        if count(graph, graph[rootA][0]) <= count(graph, graph[rootB][0]):
            graph[rootB] = graph[rootA]
            graph[pair[1]] = graph[rootA]  # path compression
        else:
            graph[rootA] = graph[rootB]
            graph[pair[0]] = graph[rootB]  # path compression


def union_find(graph: dict, pairings: list) -> dict:
    for pair in pairings:
        union(graph, pair)
    return graph
