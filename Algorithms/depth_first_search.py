def dfs_tree(tree):
    stack = [tree]

    while stack:
        current = stack.pop()

         if current:
            print(current[0])

            stack.extend([current[1][0],current[1][1]])

def dfs_trie(trie):
    stack = [trie]

    while stack:
        current = stack.pop()
        print(current[0])

        for letter in [character for character in trie[1] if character]:
            stack.extend([letter for letter in [character for character in current[1] if character]])

def dfs_adj_list(graph,visited):
    for vertex in graph:
        if vertex not in visited:
            stack = [vertex]

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited[current] = True
                    print(current)

                    for node in graph[current]:
                        stack.append(node)

def dfs_adj_mat(graph, visited):
    for node in range(len(graph)):
        stack = [node]

        while stack:
            current = stack.pop()
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
