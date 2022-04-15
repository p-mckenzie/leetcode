class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        new_positions = dict()
        for i in range(length):
            new_positions[(i+k)%length] = nums[i]

        for key, val in new_positions.items():
            nums[key] = val

        return nums
