import unittest
from unittest.mock import Mock, patch

from main import get_joke, len_joke


class TestLenJoke(unittest.TestCase):
    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "This is a joke"
        self.assertEqual(len_joke(), 14)


class TestGetJoke(unittest.TestCase):
    @patch("main.requests")
    def test_get_joke_success(self, mock_requests):
        # mocking config
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "Some joke"}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "Some joke")

    @patch("main.requests")
    def test_fail_get_joke(self, mock_requests):
        mock_response = Mock(status_code=403)
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No joke")
