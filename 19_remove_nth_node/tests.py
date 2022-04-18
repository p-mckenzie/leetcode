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
        n = 2
        
        expected = self.list_to_LL([1,2,3,5])
        actual = Solution().removeNthFromEnd(head, n)

        assert expected == actual

    def test_example_2(self):
        head = self.list_to_LL([1])
        n = 1
        
        expected = self.list_to_LL([])
        actual = Solution().removeNthFromEnd(head, n)

        assert expected == actual

    def test_example_3(self):
        head = self.list_to_LL([1,2])
        n = 1
        
        expected = self.list_to_LL([1])
        actual = Solution().removeNthFromEnd(head, n)

        assert expected == actual

    def test_example_4(self):
        head = self.list_to_LL([1,2])
        n = 2
        
        expected = self.list_to_LL([2])
        actual = Solution().removeNthFromEnd(head, n)

        assert expected == actual
