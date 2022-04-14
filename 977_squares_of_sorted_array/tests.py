import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        nums = [-4,-1,0,3,10]

        expected = [0,1,9,16,100]
        actual = Solution().sortedSquares(nums)

        assert expected == actual

    def test_example_2(self):
        nums = [-7,-3,2,3,11]

        expected = [4,9,9,49,121]
        actual = Solution().sortedSquares(nums)

        assert expected == actual