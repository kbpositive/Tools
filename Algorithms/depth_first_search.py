from DataStructures.Graph import adj_list
from DataStructures.Tree import binary_search, trie

def dfs_tree(tree):
    if tree:
        dfs_tree(tree.left)
        print(tree.val)
        dfs_tree(tree.right)

def dfs_trie(trie):
    print(trie.symbol)
    for letter in [character for character in trie.letters if character]:
        dfs_trie(letter)

def dfs_graph(graph,node,visited):
    if node in visited:
        print(visited)
        return
    visited[node] = True
    for neighbor in graph.vertices[node]:
        dfs_graph(graph,neighbor,visited)


if __name__ == '__main__':
    bs = binary_search.Tree()
    tr = trie.Tree()
    grl = adj_list.Graph({(1,2),(1,3),(1,4),(2,3),(4,3),(3,5),(4,5)})

    for word in ["hippopotamus","hypothermia","hyperthermia"]:
        tr.add(word)

    for num in range(15):
        bs.insert((num*13)%15)

    dfs_tree(bs.root)
    dfs_trie(tr.root)
    dfs_graph(grl,list(grl.vertices)[0],{})
    
    print('\npass')
