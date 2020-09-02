from DataStructures.AbstractDataTypes import tree_node


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item, node):
        if node is None:
            self.root = tree_node.Node(item, None, None)
            self.size += 1
        elif item is node.val:
            raise ValueError('Node already exists!')
        elif node.val > item:
            if node.left is None:
                node.left = tree_node.Node(item, None, None)
                self.size += 1
            else:
                self.insert(item, node.left)
        else:
            if node.right is None:
                node.right = tree_node.Node(item, None, None)
                self.size += 1
            else:
                self.insert(item, node.right)

    def remove(self, item, root):
        if root.val > item:
            root.left = self.remove(item, root.left)
        elif root.val < item:
            root.right = self.remove(item, root.right)
        else:
            if root.left is None:
                temp = root.right
                del root
                self.size -= 1
                return temp
            if root.right is None:
                temp = root.left
                del root
                self.size -= 1
                return temp
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            root.val = temp.val
            del temp
            self.size -= 1
        return root

    def search(self, item, node=None, traversal='inorder'):
        if node is None:
            return None
        if traversal == 'preorder' and node.val is not item:
            print(node.val)
            if item < node.val:
                self.search(item, node.left, traversal)
            else:
                self.search(item, node.right, traversal)
        elif traversal == 'inorder' and node.val is not item:
            if item < node.val:
                self.search(item, node.left, traversal)
            print(node.val)
            if item > node.val:
                self.search(item, node.right, traversal)
        elif traversal == 'postorder' and node.val is not item:
            if item < node.val:
                self.search(item, node.left, traversal)
            else:
                self.search(item, node.right, traversal)
            print(node.val)
        else:
            print(node.val)
            return node
