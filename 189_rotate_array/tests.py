import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3

        expected = [5,6,7,1,2,3,4]
        actual = Solution().rotate(nums, k)

        assert expected == actual

    def test_example_2(self):
        nums = [-1,-100,3,99]
        k = 2

        expected = [3,99,-1,-100]
        actual = Solution().rotate(nums, k)

        assert expected == actual
