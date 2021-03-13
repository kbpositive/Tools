class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.size = len(self.print_tree())

    def level_print(self):
        output = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current:
                output.append(current.val)
                queue.extend([i for i in [current.left,current.right] if i])
        return output

    def print_tree(self, order='in'):
        # TODO: refactor
        if self.root is None:
            return []
        else:
            orders ={n:True for n in ['pre','in','post']}
            output = []
            stack = []
            current = self.root
            if order not in orders:
                raise Exception("Invalid search order.")
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
        # if tree is not empty
        if self.root:

            # create iterator and set to root
            current = self.root

            # while a next node exists, and current value is not item
            while {0:current.left, 1:current.right}[current.val < item] and current.val != item:

                # set current node to next based on whether current.val < item
                current = {0:current.left, 1:current.right}[current.val < item]

            # if current value is equal to item, the item is a duplicate
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
        # if tree is not empty create previous
        # and current variables, both set to the root
        if self.root:
            previous = self.root
            current = previous

            # while there is a next node and the current value is not item,
            # set previous value to current and current value to next node
            while {0:current.left, 1:current.right}[current.val < item] and current.val != item:
                previous = current
                current = {0:current.left, 1:current.right}[current.val < item]

            # if current value is equal to item, current becomes
            # the deletion target with its right child as the default
            # replacement
            if current.val == item:
                replacement = current.right

                # if target has both children
                # set parent value to target
                if current.right and current.left:
                    parent = current

                    # while replacement exists and has a left child
                    # set parent value to replacement value
                    # and replacement value to its left child
                    while replacement and replacement.left:
                        parent = replacement
                        replacement = replacement.left

                    # set left child of replacement's parent
                    # to replacement's right child; set replacement's
                    # left child to the target's left child; set the
                    # replacement's right child to the parent
                    parent.left = replacement.right
                    replacement.left = current.left
                    replacement.right = parent

                # if target only has either a left or right node,
                # this node becomes the replacement
                elif current.right:
                    replacement = current.right
                elif current.left:
                    replacement = current.left

                # if current is the root, set root to the replacement node
                # otherwise set the next node
                # (based on whether previous.val < item) to the replacement node
                if current is self.root:
                    self.root = replacement
                else:
                    setattr(previous, {0:'left', 1:'right'}[previous.val < item], replacement)

                # increment tree size by 1
                self.size -= 1

        # otherwise, the item is not in the tree
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
    assert T.level_print() == [5, 2, 8, 0, 4, 6, 10, 1, 3, 7, 9]
    assert T.size == 11

    A.remove(8)
    assert A.level_print() == [5,2,9,0,4,6,10,1,3,7]

    B.remove(5)
    assert B.level_print() == [6,2,8,0,4,7,10,1,3,9]

    C.remove(0)
    assert C.level_print() == [5,2,8,1,4,6,10,3,7,9]

    D.remove(10)
    assert D.level_print() == [5,2,8,0,4,6,9,1,3,7]

    E.remove(7)
    assert E.level_print() == [5,2,8,0,4,6,10,1,3,9]

    print("Pass")
