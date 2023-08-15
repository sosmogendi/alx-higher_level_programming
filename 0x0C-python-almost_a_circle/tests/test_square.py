# tests/test_square.py

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        # Test cases for the area method
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(3)
        self.assertEqual(s2.area(), 9)

    def test_to_dictionary(self):
        # Test cases for the to_dictionary method
        s1 = Square(5, 3, 2, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 3, 'y': 2}
        self.assertEqual(s1.to_dictionary(), expected_dict)

        s2 = Square(2, 1)
        expected_dict = {'id': 1, 'size': 2, 'x': 1, 'y': 0}
        self.assertEqual(s2.to_dictionary(), expected_dict)

    def test_update(self):
        # Test cases for the update method
        s1 = Square(5, 3, 2, 10)
        s1.update(7)
        self.assertEqual(s1.id, 7)

        s2 = Square(2, 1)
        s2.update(size=4, y=2)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.y, 2)


if __name__ == "__main__":
    unittest.main()
