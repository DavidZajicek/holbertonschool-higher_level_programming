import unittest
Square = __import__('2-square').Square


class TestSquareClass(unittest.TestCase):
    """Test Suite"""

    def test_init(self):
        """Test with working value"""
        square = Square(3)
        print(type(square))
        self.assertEqual(1, len(square.__dict__))

    def test_init_no_args(self):
        """Test with no arg"""
        square = Square()
        print(type(square))
        self.assertEqual(1, len(square.__dict__))

    def test_init_wrong_type(self):
        """TypeError should be raised when passing the wrong type"""
        with self.assertRaises(TypeError):
            Square("string")

    def test_init_negative_int(self):
        """ValueError should be raised when passing a negative int"""
        with self.assertRaises(ValueError):
            Square(-1)


if __name__ == '__main__':
    unittest.main()
