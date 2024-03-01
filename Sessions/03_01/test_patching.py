import unittest
from unittest.mock import patch
from patching import greet
from patching import check

import io
import sys


class TestGreet(unittest.TestCase):
    @patch("patching.print")
    def test_greet(self, mock_print):
        greet()
        mock_print.assert_called_with("Hello, World")


class TestGreetRerouteStdOut(unittest.TestCase):
    def test_greet(self):

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        greet()
        sys.stdout = old_stdout
        output = new_stdout.getvalue()
        self.assertEqual(output, "Hello, World\n")


class TestCheck(unittest.TestCase):
    @patch("patching.random")
    @patch("patching.print")
    def test_check_lucky(self, mock_print, mock_random):
        mock_random.random.return_value = 0.8
        check()
        mock_print.assert_called_with("Congratulations")

    @patch("patching.random")
    @patch("patching.print")
    def test_check_unlucky(self, mock_print, mock_random):
        mock_random.random.return_value = 0.2
        check()
        mock_print.assert_called_with("Sorry")


if __name__ == "__main__":
    unittest.main()
