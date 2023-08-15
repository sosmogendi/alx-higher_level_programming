# tests/test_rectangle.py

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test cases for the area method
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

        r2 = Rectangle(2, 7)
        self.assertEqual(r2.area(), 14)

    def test_to_dictionary(self):
        # Test cases for the to_dictionary method
        r1 = Rectangle(5, 10)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0}
        self.assertEqual(r1.to_dictionary(), expected_dict)

        r2 = Rectangle(2, 7, 3, 4, 10)
        expected_dict = {'id': 10, 'width': 2, 'height': 7, 'x': 3, 'y': 4}
        self.assertEqual(r2.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
