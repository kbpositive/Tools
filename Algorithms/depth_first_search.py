# for dictionary graphs
def dfs_dict(graph, function, visited=None):
    if visited is None:
        visited = set()
    function(graph)
    for node in graph:
        if node not in visited:
            visited.add(node)
            dfs_dict(node, function, visited)


# for DataStructures.Components.tree.TreeNode types
def dfs_tree(tree, function):
    function(tree)
    for child in tree.node:
        if child:
            dfs_tree(child, function)
