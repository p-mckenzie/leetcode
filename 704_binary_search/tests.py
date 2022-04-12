import pytest

from implementation import Solution

class TestSolution(object):

    def test_example_1(self):
        nums = [-1,0,3,5,9,12]
        target = 9

        expected = 4
        actual = Solution().search(nums, target)

        assert expected == actual

    def test_example_2(self):
        nums = [-1,0,3,5,9,12]
        target = 2

        expected = -1
        actual = Solution().search(nums, target)

        assert expected == actual

    def test_1_num(self):
        nums = [5]
        target = 5

        expected = 0
        actual = Solution().search(nums, target)

        assert expected == actual

    def test_first_num(self):
        nums = [5,6,7,13]
        target = 5

        expected = 0
        actual = Solution().search(nums, target)

        assert expected == actual

    def test_last_num(self):
        nums = [5,6,7,13]
        target = 13

        expected = 3
        actual = Solution().search(nums, target)

        assert expected == actual

    def test_too_big(self):
        nums = [-1,0,3,5,9,12]
        target = 13

        expected = -1
        actual = Solution().search(nums, target)

        assert expected == actual