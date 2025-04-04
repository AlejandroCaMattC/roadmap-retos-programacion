import unittest

"""Unit testing in Python"""


def sum(a, b):
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, 4), 3)


unittest.main()
