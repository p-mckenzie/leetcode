class Solution:
    def moveZeroes(self, nums):
        num_zeroes = 0
        length = len(nums)
        for i in range(length):
            if nums[i]==0:
                num_zeroes+=1
            else:
                nums[i-num_zeroes] = nums[i]

        for i in range(num_zeroes):
            nums[length-i-1] = 0
            
        return nums