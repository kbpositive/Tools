class Node:
    def __init__(self, val, child=None):
        self.val = val
        self.child = child


class List:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size
        self.tail = self.head
        while self.tail:
            if self.tail.child == None:
                break
            self.tail = self.tail.child

    def print_list(self):
        listToPrint = []
        current = self.head

        while current:
            listToPrint.append(current.val)
            current = current.child

        return listToPrint

    def insert_at_index(self, item, index=None):
        # set default index to the end of the list
        if index is None:
            index = self.length

        # create new node with val=item, pointing to head
        current = Node(item, self.head)

        # iterate until either the list node is None or the index is 0
        while current.child and (index > 0):
            current = current.child
            index -= 1

        # if index is not 0, the given index is out of the lists range
        if index != 0:
            raise Exception("Index out of range.")

        # if index is 0, the insertion point of the list has been reached

        # if the current node is not pointing to the list's head,
        # the list is not empty and the insertion point is the child node
        if current.child != self.head:
            current.child = Node(item, current.child)

            # push current node forward by 1 to check if it's a tail node.
            current = current.child

        # if the current node is pointing to the list's head,
        # the list is empty or the insertion point is the head.
        # In this case, we can make the current/new node the head.
        else:
            self.head = current

        if not current.child:
            self.tail = current

        # increment the list's size parameter
        self.size += 1

    def insert_at_item(self, item, search=None):
        current = Node(item, self.head)

        while current.child and current.child.val != search:
            current = current.child

        if search and current.child is None:
            raise Exception("Item not found")

        if current.child != self.head:
            current.child = Node(item, current.child)
            current = current.child
        else:
            self.head = current

        if not current.child:
            self.tail = current

        self.size += 1

    def remove_index(self, index):
        if not self.head:
            return

        current = Node(None, self.head)

        while current.child and (index > 0):
            current = current.child
            index -= 1

        if index != 0:
            raise Exception("Index out of range.")

        if current.child != self.head:
            current.child = current.child.child
        else:
            self.head = current.child.child

        if current and not current.child:
            self.tail = current

        self.size -= 1

    def remove_item(self, search):
        if not self.head:
            return

        current = Node(None, self.head)

        while current.child and current.child.val != search:
            current = current.child

        if current.child is None or current.child.val != search:
            raise Exception("Item not found")

        if current.child != self.head:
            current.child = current.child.child
        else:
            self.head = current.child.child

        if current and not current.child:
            self.tail = current

        self.size -= 1

    @property
    def length(self):
        return self.size

    @property
    def tailEnd(self):
        return self.tail


if __name__ == "__main__":
    L = List()
    items = [3, 2, 1, 9, 8, 7, 6, 5, 4, 0]

    for item in items:
        L.insert_at_index(item, L.length)

    assert L.print_list() == [3, 2, 1, 9, 8, 7, 6, 5, 4, 0]
    assert L.length == 10
    assert L.tail.val == 0

    G = List()

    G.insert_at_index(3, 0)
    G.insert_at_index(2, 1)
    G.insert_at_index(1, 0)

    L.insert_at_index(0, 2)
    L.insert_at_index(2, 0)
    L.insert_at_index(4, 1)

    assert G.print_list() == [1, 3, 2]
    assert L.print_list() == [2, 4, 3, 2, 0, 1, 9, 8, 7, 6, 5, 4, 0]
    assert G.length == 3
    assert G.tail.val == 2
    assert L.length == 13
    assert L.tail.val == 0

    G = List()

    G.insert_at_item(3, None)
    G.insert_at_item(5, 3)
    G.insert_at_item(7, 5)
    G.insert_at_item(4, 3)
    G.insert_at_item(9, 5)

    L.insert_at_item(5, 5)
    L.insert_at_item(0, 0)
    L.insert_at_item(1, 1)

    assert G.print_list() == [7, 9, 5, 4, 3]
    assert L.print_list() == [2, 4, 3, 2, 0, 0, 1, 1, 9, 8, 7, 6, 5, 5, 4, 0]
    assert G.length == 5
    assert G.tail.val == 3
    assert L.length == 16
    assert L.tail.val == 0

    L.remove_item(7)
    L.remove_item(6)
    L.remove_item(0)
    L.remove_item(0)
    L.remove_item(0)
    L.remove_item(1)

    assert L.print_list() == [2, 4, 3, 2, 1, 9, 8, 5, 5, 4]
    assert L.length == 10
    assert L.tail.val == 4

    for i in range(9, 9 - 3, -1):
        L.remove_index(i)

    assert L.print_list() == [2, 4, 3, 2, 1, 9, 8]
    assert L.length == 7
    assert L.tail.val == 8

    print("Pass")
