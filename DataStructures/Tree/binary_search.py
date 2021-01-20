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
        previous = self.root

        if previous:
            current = {0:previous.left, 1:previous.right}[previous.val < item]

            while current:
                previous = current
                current = {0:previous.left, 1:previous.right}[previous.val < item]

            if previous.val == item:
                raise Exception("Item already exists.")

            if previous.val < item:
                previous.right = Node(item)

            else:
                previous.left = Node(item)

        else:
            self.root = Node(item)

        self.size += 1

    def remove(self, item):
        current = self.root

        if current:
            next = {0:current.left, 1:current.right}[current.val < item]

            while next:
                previous = current
                current = next

                if current.val != item:
                    next = {0:current.left, 1:current.right}[current.val < item]
                    
                else:
                    min = current.right

                    if current.right:
                        while min and min.left:
                            min = min.left

                        min.left = current.left
                        min.right = current.right

                    elif current.left:
                        min = current.left

                    if previous.val < item:
                        previous.right = min

                    else:
                        previous.left = min

                    return

        raise Exception("Item not in tree.")

    def print_tree(self, order='in'):
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

    assert T.print_tree('pre') == [5, 2, 0, 1, 4, 3, 8, 6, 7, 10]
    assert T.print_tree('in') == [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
    assert T.print_tree('post') == [1, 0, 3, 4, 2, 7, 6, 10, 8, 5]
    assert T.print_tree('level') == [5, 2, 8, 0, 4, 6, 10, 1, 3, 7]
    assert T.size == 10

    T.remove(2)
    print(T.print_tree('pre'))
    print("Pass")
