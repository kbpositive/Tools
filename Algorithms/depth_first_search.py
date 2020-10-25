# for DataStructures.Tree.Nodes.regular types
def dfs_tree(tree, function):
    function(tree)
    if tree.left:
        dfs_tree(tree.left, function)
    if tree.right:
        dfs_tree(tree.right, function)
