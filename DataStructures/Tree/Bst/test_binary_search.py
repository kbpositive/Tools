import unittest
import binary_search


class TestBst(unittest.TestCase):
    def test_insert(self):
        T = binary_search.Tree()
        for value in [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]:
            T.insert(value)
        result = []
        stack = [[T.root, None]]
        while stack:
            current = stack.pop()
            if current[0]:
                stack.extend(
                    [[current[0].right, current[0].val], [current[0].left, None]]
                )
            if current[1] is not None:
                result.append(current[1])
        self.assertEqual(result, [num for num in range(11)])

    def test_remove(self):
        T = binary_search.Tree()
        for value in [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]:
            T.insert(value)
        T.remove(8)
        T.remove(5)
        T.remove(0)
        T.remove(10)
        T.remove(7)
        result = []
        stack = [[T.root, None]]
        while stack:
            current = stack.pop()
            if current[0]:
                stack.extend(
                    [[current[0].right, current[0].val], [current[0].left, None]]
                )
            if current[1] is not None:
                result.append(current[1])
        self.assertEqual(result, [1, 2, 3, 4, 6, 9])

    def test_print_tree_pre(self):
        T = binary_search.Tree()
        for value in [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]:
            T.insert(value)

        self.assertEqual(T.print_tree("pre"), [5, 2, 0, 1, 4, 3, 8, 6, 7, 10, 9])

        with self.assertRaises(ValueError):
            T.print_tree("")

    def test_print_tree_in(self):
        T = binary_search.Tree()
        for value in [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]:
            T.insert(value)

        self.assertEqual(T.print_tree("in"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        with self.assertRaises(ValueError):
            T.print_tree("")

    def test_print_tree_post(self):
        T = binary_search.Tree()
        for value in [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]:
            T.insert(value)

        self.assertEqual(T.print_tree("post"), [1, 0, 3, 4, 2, 7, 6, 9, 10, 8, 5])

        with self.assertRaises(ValueError):
            T.print_tree("")

    def test_print_tree_level(self):
        T = binary_search.Tree()
        for value in [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]:
            T.insert(value)

        self.assertEqual(T.print_tree("level"), [5, 2, 8, 0, 4, 6, 10, 1, 3, 7, 9])

        with self.assertRaises(ValueError):
            T.print_tree("")


if __name__ == "__main__":
    unittest.main()