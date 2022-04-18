import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        s = "Let's take LeetCode contest"

        expected = "s'teL ekat edoCteeL tsetnoc"
        actual = Solution().reverseWords(s)

        assert expected == actual
