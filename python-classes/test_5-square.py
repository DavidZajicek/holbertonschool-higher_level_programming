import unittest
Square = __import__('5-square').Square


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

    def test_area_method(self):
        """Print the Square's total area"""
        my_square = Square(3)
        self.assertEqual(9, my_square.area())

    def test_size_get_set(self):
        """Tests the size's getter and setter methods"""
        my_square = Square(3)
        self.assertEqual(9, my_square.area())
        my_square.size = 4
        self.assertEqual(16, my_square.area())
        self.assertEqual(4, my_square.size)

    def test_setter_wrong_type(self):
        """TypeError should be raised when passing the wrong type"""
        my_square = Square()
        with self.assertRaises(TypeError):
            my_square.size = "string"

    def test_setter_negative_int(self):
        """ValueError should be raised when passing a negative int"""
        my_square = Square()
        with self.assertRaises(ValueError):
            my_square.size = -1

    def test_my_print(self):
        """Test Print Square"""
        Square().my_print()
        Square(3).my_print()


if __name__ == '__main__':
    unittest.main()