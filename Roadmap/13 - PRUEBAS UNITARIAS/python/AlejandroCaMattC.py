import unittest
from datetime import datetime

"""Unit testing in Python"""


def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, 4), 3)
        self.assertEqual(sum(0, 0), 0)
        self.assertAlmostEqual(sum(10.2, 11.6), 21.8)

    def test_sum_types(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)


# unittest.main()


"""Exercise"""

data = {
    "name": "John",
    "age": 30,
    "birth_date": datetime.strptime("1993-05-14", "%Y-%m-%d").date(),
    "programming_languages": ["Python", "Java", "C++"],
}


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "John",
            "age": 30,
            "birth_date": datetime.strptime("1993-05-14", "%Y-%m-%d").date(),
            "programming_languages": ["Python", "Java", "C++"],
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], datetime.date)
        self.assertIsInstance(self.data["programming_languages"], list)


unittest.main()
