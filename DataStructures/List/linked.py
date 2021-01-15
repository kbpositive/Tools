class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def print_list(self):
        listToPrint = []
        current = self.head

        while current:
            listToPrint.append(current.val)
            current = current.next

        return listToPrint

    def insert_at_index(self, item, index):
        current = Node(item, self.head)

        while current.next and (index > 0):
            current = current.next
            index -= 1

        if index != 0:
            raise Exception("Index out of range.")

        if current.next != self.head:
            current.next = Node(item, current.next)
        else:
            self.head = current

        self.size += 1

    def insert_at_item(self, item, search):
        current = Node(item, self.head)

        while current.next and current.next.val != search:
            current = current.next

        if search and current.next is None:
            raise Exception("Item not found")

        if current.next != self.head:
            current.next = Node(item, current.next)
        else:
            self.head = current

        self.size += 1

    def remove_index(self, index):
        if self.head:
            current = Node(None,self.head)

            while current.next and (index > 0):
                current = current.next
                index -= 1

            if index != 0:
                raise Exception("Index out of range.")

            if current.next != self.head:
                current.next = current.next.next
            else:
                self.head = current.next.next

            self.size -= 1

    def remove_item(self, search):
        if self.head:
            current = Node(None,self.head)

            while current.next and current.next.val != search:
                current = current.next

            if current.next is None or current.next.val != search:
                raise Exception("Item not found")

            if current.next != self.head:
                current.next = current.next.next
            else:
                self.head = current.next.next

            self.size -= 1

    @property
    def length(self):
        return self.size

if __name__ == '__main__':
    L = List()
    items = [3,2,1,9,8,7,6,5,4,0]

    for item in items:
        L.insert_at_index(item,L.length)

    assert L.print_list() == [3,2,1,9,8,7,6,5,4,0]
    assert L.length == 10

    G = List()

    G.insert_at_index(3,0)
    G.insert_at_index(2,1)
    G.insert_at_index(1,0)

    L.insert_at_index(0, 2)
    L.insert_at_index(2, 0)
    L.insert_at_index(4, 1)

    assert G.print_list() == [1,3,2]
    assert L.print_list() == [2,4,3,2,0,1,9,8,7,6,5,4,0]
    assert G.length == 3
    assert L.length == 13

    G = List()

    G.insert_at_item(3,None)
    G.insert_at_item(5,3)
    G.insert_at_item(7,5)
    G.insert_at_item(4,3)
    G.insert_at_item(9,5)

    L.insert_at_item(5, 5)
    L.insert_at_item(0, 0)
    L.insert_at_item(1, 1)

    assert G.print_list() == [7,9,5,4,3]
    assert L.print_list() == [2,4,3,2,0,0,1,1,9,8,7,6,5,5,4,0]
    assert G.length == 5
    assert L.length == 16

    L.remove_item(7)
    L.remove_item(6)
    L.remove_item(0)
    L.remove_item(1)

    assert L.print_list() == [2,4,3,2,0,1,9,8,5,5,4,0]
    assert L.length == 12

    for i in range(3):
        L.remove_index(i)

    assert L.print_list() == [4,2,1,9,8,5,5,4,0]
    assert L.length == 9
    
    print("Pass")
