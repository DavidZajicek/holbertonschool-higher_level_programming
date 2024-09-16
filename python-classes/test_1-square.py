import unittest
Square = __import__('1-square').Square


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


if __name__ == '__main__':
    unittest.main()
