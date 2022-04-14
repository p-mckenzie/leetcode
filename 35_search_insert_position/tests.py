import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        nums = [1,3,5,6]
        target = 5

        expected = 2
        actual = Solution().searchInsert(nums, target)

        assert expected == actual

    def test_example_2(self):
        nums = [1,3,5,6]
        target = 2

        expected = 1
        actual = Solution().searchInsert(nums, target)

        assert expected == actual

    
    def test_example_3(self):
        nums = [1,3,5,6]
        target = 7

        expected = 4
        actual = Solution().searchInsert(nums, target)

        assert expected == actual
    
    def test_example_4(self):
        nums = [1,3,5,6]
        target = 0

        expected = 0
        actual = Solution().searchInsert(nums, target)

        assert expected == actual
    
    def test_example_5(self):
        nums = [1,3,5]
        target = 1

        expected = 0
        actual = Solution().searchInsert(nums, target)

        assert expected == actual

    