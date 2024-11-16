import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestUtils(unittest.TestCase):

    def test_access_nested_map(self):
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)

    @patch('requests.get')
    def test_get_json(self, mock_get):
        mock_response = {'key': 'value'}
        mock_get.return_value.json.return_value = mock_response

        result = get_json('http://example.com/api')
        self.assertEqual(result, mock_response)

    def test_memoize(self):
        class MyClass:
            call_count = 0

            @memoize
            def a_method(self):
                MyClass.call_count += 1
                return 42
