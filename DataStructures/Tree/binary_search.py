class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.size = len(self.print_tree())

    def print_tree(self, order='in'):
        if self.root is None:
            return []
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


    def insert(self, item):
        if self.root:
            # create iterator and set to root
            current = self.root

            # check for duplicates
            if current.val == item:
                raise Exception("Item already exists.")

            # while a next node exists, get next node based on whether
            # current value < item
            while {0:current.left, 1:current.right}[current.val < item]:
                current = {0:current.left, 1:current.right}[current.val < item]

                # check for duplicates at each step
                if current.val == item:
                    raise Exception("Item already exists.")

            # set next value (based on whether current value < item) to new node
            setattr(current, {0:'left', 1:'right'}[current.val < item], Node(item))

        # otherwise, set root to the inserted item
        else:
            self.root = Node(item)

        # increment tree size by 1
        self.size += 1

    def remove(self, item):
        # create iterator and set to root
        current = self.root

        # if tree is not empty
        if current:
            next = self.root

            while next:
                previous = current
                current = next

                if current.val != item:
                    next = {0:current.left, 1:current.right}[current.val < item]

                else:
                    prev = current
                    min = current.right

                    if current.right and current.left:
                        while min and min.left:
                            prev = min
                            min = min.left
                        prev.left = min.right
                        min.left = current.left
                        min.right = prev
                    elif current.right:
                        min = current.right
                    elif current.left:
                        min = current.left

                    if previous.val < item:
                        previous.right = min
                    elif item < previous.val:
                        previous.left = min
                    elif previous is self.root:
                        self.root = min

                    self.size -= 1

        # otherwise the item to be deleted is not in the tree
        else:
            raise Exception("Item not in tree.")



if __name__ == '__main__':
    A = Tree()
    B = Tree()
    C = Tree()
    D = Tree()
    E = Tree()
    T = Tree()
    vals = [5,2,4,3,0,1,8,6,7,10,9]
    for value in vals:
        A.insert(value)
        B.insert(value)
        C.insert(value)
        D.insert(value)
        E.insert(value)
        T.insert(value)

    assert T.print_tree('pre') == [5, 2, 0, 1, 4, 3, 8, 6, 7, 10, 9]
    assert T.print_tree('in') == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert T.print_tree('post') == [1, 0, 3, 4, 2, 7, 6, 9, 10, 8, 5]
    assert T.print_tree('level') == [5, 2, 8, 0, 4, 6, 10, 1, 3, 7, 9]
    assert T.size == 11

    A.remove(8)
    assert A.print_tree('level') == [5,2,9,0,4,6,10,1,3,7]

    B.remove(5)
    assert B.print_tree('level') == [6,2,8,0,4,7,10,1,3,9]

    C.remove(0)
    assert C.print_tree('level') == [5,2,8,1,4,6,10,3,7,9]

    D.remove(10)
    assert D.print_tree('level') == [5,2,8,0,4,6,9,1,3,7]

    E.remove(7)
    assert E.print_tree('level') == [5,2,8,0,4,6,10,1,3,9]

    print("Pass")
