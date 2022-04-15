import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        nums = [0,1,0,3,12]

        expected = [1,3,12,0,0]
        actual = Solution().moveZeroes(nums)

        assert expected == actual

    def test_example_2(self):
        nums = [0]

        expected = [0]
        actual = Solution().moveZeroes(nums)

        assert expected == actual
