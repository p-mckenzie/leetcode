import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        n = 5
        bad = 4

        expected = 4
        actual = Solution(bad).firstBadVersion(n)

        assert expected == actual

    def test_example_2(self):
        n = 1
        bad = 1

        expected = 1
        actual = Solution(bad).firstBadVersion(n)

        assert expected == actual

    def test_no_solution(self):
        n = 4
        bad = 7

        expected = -1
        actual = Solution(bad).firstBadVersion(n)

        assert expected == actual