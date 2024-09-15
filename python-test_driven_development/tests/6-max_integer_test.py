import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerMethod(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(4, max_integer([1, 2, 3, 4]))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            max_integer(123)

    def test_none(self):
        self.assertEqual(None, max_integer([]))


if __name__ == '__main__':
    unittest.main()
