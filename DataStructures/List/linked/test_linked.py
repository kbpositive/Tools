import unittest
import linked

class TestLinkedList(unittest.TestCase):

    def test_insert_at_index(self):
        L = linked.LinkedList()

        with self.subTest():
            self.assertEqual(L.length, 0)
        with self.subTest():
            self.assertEqual(L.tailEnd, None)

        L.insert_at_index(1, 0)

        with self.subTest():
            self.assertEqual(L.length, 1)
        with self.subTest():
            self.assertEqual(L.tailEnd, 1)

        L.insert_at_index(5, 1)

        with self.subTest():
            self.assertEqual(L.length, 2)
        with self.subTest():
            self.assertEqual(L.tailEnd, 5)

        L.insert_at_index(7, 0)

        with self.subTest():
            self.assertEqual(L.length, 3)
        with self.subTest():
            self.assertEqual(L.tailEnd, 5)
    
    def test_insert_at_item(self):
        L = linked.LinkedList()

        with self.subTest():
            self.assertEqual(L.length, 0)
        with self.subTest():
            self.assertEqual(L.tailEnd, None)

        L.insert_at_item(1, None)

        with self.subTest():
            self.assertEqual(L.length, 1)
        with self.subTest():
            self.assertEqual(L.tailEnd, 1)

        L.insert_at_item("f", None)

        with self.subTest():
            self.assertEqual(L.length, 2)
        with self.subTest():
            self.assertEqual(L.tailEnd, "f")

        L.insert_at_item([10], "f")

        with self.subTest():
            self.assertEqual(L.length, 3)
        with self.subTest():
            self.assertEqual(L.tailEnd, "f")

    def test_remove_index(self):
        L = linked.LinkedList()
        L.insert_at_index(1, 0)
        L.insert_at_index(5, 1)
        L.insert_at_index(7, 0)

        with self.subTest():
            self.assertEqual(L.length, 3)
        with self.subTest():
            self.assertEqual(L.tailEnd, 5)
        
        L.remove_index(2)

        with self.subTest():
            self.assertEqual(L.length, 2)
        with self.subTest():
            self.assertEqual(L.tailEnd, 1)
        
        L.remove_index(1)

        with self.subTest():
            self.assertEqual(L.length, 1)
        with self.subTest():
            self.assertEqual(L.tailEnd, 7)
        
        L.remove_index(0)

        with self.subTest():
            self.assertEqual(L.length, 0)
        with self.subTest():
            self.assertEqual(L.tailEnd, None)

    # test remove at item
    def test_remove_item(self):
        pass
    
    # below code to be deleted
    L = linked.LinkedList()
    items = [3, 2, 1, 9, 8, 7, 6, 5, 4, 0]

    for item in items:
        L.insert_at_index(item, L.length)

    assert L.print_list() == [3, 2, 1, 9, 8, 7, 6, 5, 4, 0]
    assert L.length == 10
    assert L.tail.val == 0

    G = linked.LinkedList()

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

    G = linked.LinkedList()

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

if __name__ == "__main__":
    unittest.main()
