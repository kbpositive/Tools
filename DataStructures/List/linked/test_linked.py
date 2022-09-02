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

    def test_remove_item(self):
        L = linked.LinkedList()
        L.insert_at_item(1, None)
        L.insert_at_item("f", 1)
        L.insert_at_item(["h"], None)

        with self.subTest():
            self.assertEqual(L.length, 3)
        with self.subTest():
            self.assertEqual(L.tailEnd, ["h"])
        
        L.remove_item(["h"])

        with self.subTest():
            self.assertEqual(L.length, 2)
        with self.subTest():
            self.assertEqual(L.tailEnd, 1)
        
        L.remove_item(1)

        with self.subTest():
            self.assertEqual(L.length, 1)
        with self.subTest():
            self.assertEqual(L.tailEnd, "f")
        
        L.remove_item("f")

        with self.subTest():
            self.assertEqual(L.length, 0)
        with self.subTest():
            self.assertEqual(L.tailEnd, None)

if __name__ == "__main__":
    unittest.main()
