class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
            self.size += 1
            return
        current = self.root
        while current.val != item:
            if current.val < item:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(item)
                    self.size += 1
                    return
            elif current.val > item:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(item)
                    self.size += 1
                    return
        raise Exception("Item already exists.")

    def remove_node(self, item, node=None):
        if node is None:
            return node
        elif node.val > item:
            node.left = self.remove_node(item, node.left)
        elif node.val < item:
            node.right = self.remove_node(item, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                self.size -= 1
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                self.size -= 1
                return temp
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.val = temp.val
            temp = None
            self.size -= 1
        return node

    def remove(self, item):
        self.remove_node(item, self.root)

    def traverse(self, order='in'):
        if self.root is None:
            raise Exception("Empty Tree.")
        else:
            orders ={n:True for n in ['pre','in','post','level']}
            output = []
            stack = []
            current = self.root
            if order not in orders:
                raise Exception("Invalid search order.")
            elif order == 'level':
                queue = [current]
                while queue:
                    current = queue.pop(0)
                    output.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            else:
                while True:
                    while current:
                        stack.append(current)
                        if order == 'pre':
                            output.append(stack[-1].val)
                        current = current.left
                        if current is None:
                            if order == 'in':
                                output.append(stack[-1].val)
                            current = stack[-1].right
                    while stack and current == stack[-1].right:
                        if order == 'post':
                            output.append(stack[-1].val)
                        current = stack.pop()
                    if stack:
                        if order == 'in':
                            output.append(stack[-1].val)
                        current = stack[-1].right
                    else:
                        break
            return output

    def find_node(self, item, node=None):
        if node is None:
            raise ValueError('Item not found.')
        elif node.val != item:
            if item < node.val:
                return self.find_node(item, node.left)
            else:
                return self.find_node(item, node.right)
        else:
            return node

    def find(self, item):
        return self.find_node(item, self.root)

if __name__ == '__main__':
    T = Tree()
    vals = [5,2,4,3,0,1,8,6,7,10]
    for value in vals:
        T.insert(value)

    assert T.traverse('pre') == [5, 2, 0, 1, 4, 3, 8, 6, 7, 10]
    assert T.traverse('in') == [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
    assert T.traverse('post') == [1, 0, 3, 4, 2, 7, 6, 10, 8, 5]
    assert T.traverse('level') == [5, 2, 8, 0, 4, 6, 10, 1, 3, 7]

    print("Pass")
