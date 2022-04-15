import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        s = ["h","e","l","l","o"]

        expected = ["o","l","l","e","h"]
        actual = Solution().reverseString(s)

        assert expected == actual

    def test_example_1(self):
        s = ["H","a","n","n","a","h"]

        expected = ["h","a","n","n","a","H"]
        actual = Solution().reverseString(s)

        assert expected == actual
