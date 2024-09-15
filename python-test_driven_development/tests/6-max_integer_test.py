import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerMethod(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(4, max_integer([1, 2, 3, 4]))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_max_first(self):
        self.assertEqual(4, max_integer([4, 3, 2, 1]))

    def test_max_mid(self):
        self.assertEqual(4, max_integer([1, 4, 3, 2]))

    def test_negative(self):
        self.assertEqual(4, max_integer([1, 2, 4, -1]))

    def test_only_negatives(self):
        self.assertEqual(-1, max_integer([-4, -3, -2, -1]))

    def test_short_list(self):
        self.assertEqual(1, max_integer([1]))


if __name__ == '__main__':
    unittest.main()
