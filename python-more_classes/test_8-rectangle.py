import unittest
Rectangle = __import__('8-rectangle').Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Suite"""

    def test_init(self):
        """Test with working value"""
        rectangle = Rectangle(3)
        print(type(rectangle))
        self.assertEqual(2, len(rectangle.__dict__))

    def test_init_no_args(self):
        """Test with no arg"""
        rectangle = Rectangle()
        print(type(rectangle))
        self.assertEqual(2, len(rectangle.__dict__))

    def test_methods(self):
        """Test the methods"""
        rectangle = Rectangle(2, 2)
        print(f"Area: {rectangle.area()}\nPerimeter: {rectangle.perimeter()}")
        rectangle.width = 0
        print(f"Area: {rectangle.area()}\nPerimeter: {rectangle.perimeter()}")
        rectangle.height = 0
        rectangle.width = 1
        print(f"Area: {rectangle.area()}\nPerimeter: {rectangle.perimeter()}")
        rectangle.width = 0
        rectangle.height = 0
        print(f"Area: {rectangle.area()}\nPerimeter: {rectangle.perimeter()}")
        rectangle.height = 2
        rectangle.width = 5
        print(str(rectangle))
        print(repr(rectangle))
        print(rectangle)

    def test_repr(self):
        rect = Rectangle(2, 2)
        new_rect = eval(repr(rect))
        self.assertEqual(type(rect), type(new_rect))

    def test_compare(self):
        my_rectangle_1 = Rectangle(8, 4)
        my_rectangle_2 = Rectangle(2, 3)

        if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
            print("my_rectangle_1 is bigger or equal to my_rectangle_2")
        else:
            print("my_rectangle_2 is bigger than my_rectangle_1")

        my_rectangle_2.width = 10
        my_rectangle_2.height = 5
        if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
            print("my_rectangle_1 is bigger or equal to my_rectangle_2")
        else:
            print("my_rectangle_2 is bigger than my_rectangle_1")


if __name__ == '__main__':
    unittest.main()
