from DataStructures.AbstractDataTypes import tree


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.func = print

    def insert(self, item, node):
        if node is None:
            return tree.Node(item, None, None)
        else:
            if item is node.val:
                return node
            elif node.val < item:
                node.right = self.insert(item, node.right)
                self.size += 1
            else:
                node.left = self.insert(item, node.left)
                self.size += 1
        return node

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

    def traversal(self, node=None, order='in'):
        if node is None:
            return None
        if order == 'pre':
            self.func(node.val)
        self.traversal(node.left, order)
        if order == 'in':
            self.func(node.val)
        self.traversal(node.right, order)
        if order == 'post':
            self.func(node.val)

    def find(self, item, node=None):
        if node is None:
            return 'Item not found.'
        elif node.val != item:
            if item < node.val:
                return self.find(item, node.left)
            else:
                return self.find(item, node.right)
        else:
            return node
