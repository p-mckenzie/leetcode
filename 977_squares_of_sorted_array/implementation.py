class Solution:
    def sortedSquares(self, nums):
        final = []

        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            left = nums[left_index]
            right = nums[right_index]

            if abs(nums[left_index]) >= abs(nums[right_index]):
                final.append(left**2)
                left_index += 1
            else:
                final.append(right**2)
                right_index -= 1

        return final[::-1]