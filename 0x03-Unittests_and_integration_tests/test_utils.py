import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"a": {"b": {"c": 2}}}, ["a", "b", "c"], 2),
        ({"a": {"b": {"d": 3}}}, ["a", "b", "d"], 3),
        ({"a": {"b": {"d": 4}}}, ["a", "b", "d"], 4),
        ({"a": {"b": {"e": 5}}}, ["a", "b", "e"], 5),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
