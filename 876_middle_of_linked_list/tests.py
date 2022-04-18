import pytest

from implementation import Solution, ListNode

class TestSolution(object):

    def list_to_LL(self, arr):
        if len(arr) < 1:
            return None

        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=self.list_to_LL(arr[1:]))

    def test_example_1(self):
        head = self.list_to_LL([1,2,3,4,5])
        
        expected = self.list_to_LL([3,4,5])
        actual = Solution().middleNode(head)

        assert expected == actual

    def test_example_2(self):
        head = self.list_to_LL([1,2,3,4,5,6])
        
        expected = self.list_to_LL([4,5,6])
        actual = Solution().middleNode(head)

        assert expected == actual
