class Solution:
    def search(self, nums, target):
        
        lower_index = 0
        upper_index = len(nums)-1
        
        while lower_index <= upper_index:

            inspect_index = (upper_index+lower_index) // 2
            inspect_value = nums[inspect_index]
            
            if inspect_value==target:
                return inspect_index
            elif inspect_value < target:
                # target is larger
                lower_index = inspect_index + 1
            else:
                # target is smaller
                upper_index = inspect_index - 1

        return -1