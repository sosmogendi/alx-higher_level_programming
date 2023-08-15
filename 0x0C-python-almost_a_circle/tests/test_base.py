# tests/test_base.py

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        # Test cases for the to_json_string method
        list_dicts = [{'id': 1, 'x': 2, 'y': 3}, {'id': 2, 'x': 4, 'y': 5}]
        expected_json =
        '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), "[]")

    def test_from_json_string(self):
        # Test cases for the from_json_string method
        json_string = '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]'
        expected_list = [{'id': 1, 'x': 2, 'y': 3}, {'id': 2, 'x': 4, 'y': 5}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

        empty_json = "[]"
        self.assertEqual(Base.from_json_string(empty_json), [])

    def test_create(self):
        # Test cases for the create method
        dict1 = {'id': 1, 'width': 5, 'height': 10}
        instance1 = Base.create(**dict1)
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance1.width, 5)
        self.assertEqual(instance1.height, 10)

        dict2 = {'id': 2, 'size': 7}
        instance2 = Base.create(**dict2)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance2.size, 7)


if __name__ == "__main__":
    unittest.main()
