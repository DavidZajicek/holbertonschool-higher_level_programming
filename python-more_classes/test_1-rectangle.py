import unittest
Rectangle = __import__('1-rectangle').Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Suite"""

    def test_init(self):
        """Test with working value"""
        rectangle = Rectangle(3)
        print(type(rectangle))
        self.assertEqual(1, len(rectangle.__dict__))

    def test_init_no_args(self):
        """Test with no arg"""
        rectangle = Rectangle()
        print(type(rectangle))
        self.assertEqual(1, len(rectangle.__dict__))


if __name__ == '__main__':
    unittest.main()
