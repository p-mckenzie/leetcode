import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        nums = [2,7,11,15]
        target = 9

        expected = [1,2]
        actual = Solution().twoSum(nums, target)

        assert expected == actual

    def test_example_2(self):
        nums = [2,3,4]
        target = 6

        expected = [1,3]
        actual = Solution().twoSum(nums, target)

        assert expected == actual

    def test_example_3(self):
        nums = [-1,0]
        target = -1

        expected = [1,2]
        actual = Solution().twoSum(nums, target)

        assert expected == actual


    def test_example_4(self):
        nums = [0,0,3,4]
        target = 0

        expected = [1,2]
        actual = Solution().twoSum(nums, target)

        assert expected == actual
