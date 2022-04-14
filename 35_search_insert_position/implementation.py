class Solution:
    def searchInsert(self, nums, target):
        
        lower_index = 0
        upper_index = len(nums)-1
        
        while lower_index <= upper_index:

            inspect_index = (upper_index+lower_index) // 2
            inspect_distance = target - nums[inspect_index]
            
            if inspect_distance == 0:
                return inspect_index
            elif inspect_distance > 0:
                # go right
                lower_index = inspect_index + 1
            else:
                # go left
                upper_index = inspect_index - 1

        if inspect_distance < 0:
            return lower_index
        else:
            return upper_index + 1