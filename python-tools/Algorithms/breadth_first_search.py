from collections import deque

def bfs_tree(tree):
    queue = deque([tree])

    while queue:
        current = queue.popleft()

        if current:
            print(current[0])

            queue.extend([current[1][0],current[1][1]])

def bfs_trie(trie):
    queue = deque([trie])

    while queue:
        current = queue.popleft()
        print(current[0])

        queue.extend([character for character in current[1] if character])

def bfs_adj_list(graph,visited):
    for vertex in graph:
        if vertex not in visited:
            queue = deque([vertex])

            while queue:
                current = queue.popleft()

                if current not in visited:
                    visited[current] = True
                    print(current)

                    queue.extend(list(graph[current]))

def bfs_adj_mat(graph, visited):
    for node in range(len(graph)):
        queue = deque([node])

        while queue:
            current = queue.popleft()

            if current not in visited:
                visited[current] = True
                print(current)

                index = 0
                while index < len(graph[current]) and (graph[current][index] == 0 or index in visited):
                    index += 1

                if index < len(graph[current]):
                    queue.append(index)


if __name__ == '__main__':
    from DataStructures import quick_data_structures as qds

    bs = qds.tree(9)
    tr = qds.trie(["hippopotamus","hypothermia","hyperthermia"])
    al = qds.adj_list(7,15,directed=True,acyclic=False)
    am = qds.adj_mat(5,15,directed=True,acyclic=False,weighted=True)

    bfs_tree(bs)
    bfs_trie(tr)
    bfs_adj_list(al,{})
    bfs_adj_mat(am,{})

    print('\npass')
