import unittest
inheritance = __import__('0-lookup')


class TestSquareClass(unittest.TestCase):
    """Test Suite"""

    def test_init(self):
        """Test with working value"""
        print(inheritance.lookup(int))
        print(inheritance.lookup(float))
        print(inheritance.lookup(object))


if __name__ == '__main__':
    unittest.main()
