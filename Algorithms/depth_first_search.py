def dfs_tree(tree):
    if tree:
        dfs_tree(tree[1][0])
        print(tree[0])
        dfs_tree(tree[1][1])

def dfs_trie(trie):
    print(trie[0])
    for letter in [character for character in trie[1] if character]:
        dfs_trie(letter)

def dfs_adj_list(graph,visited):
    for vertex in graph:
        if vertex in visited:
            continue
        visited[vertex] = True
        print(vertex)
        dfs_adj_list(graph[vertex],visited)

def dfs_adj_mat(graph, visited):
    for node in range(len(graph)):
        current = node
        stack = [current]
        while stack:
            current = stack.pop(0)
            if current not in visited:
                visited[current] = True
                print(current)
                index = 0
                while index < len(graph[current]) and (graph[current][index] == 0 or index in visited):
                    index += 1
                if index < len(graph[current]):
                    stack.append(index)


if __name__ == '__main__':
    from DataStructures import quick_data_structures as qds

    bs = qds.tree(25)
    tr = qds.trie(["hippopotamus","hypothermia","hyperthermia"])
    al = qds.adj_list(7,15,directed=True,acyclic=False)
    am = qds.adj_mat(10,50,directed=True,acyclic=False,weighted=True)

    dfs_tree(bs)
    dfs_trie(tr)
    dfs_adj_list(al,{})
    dfs_adj_mat(am,{})

    print('\npass')
