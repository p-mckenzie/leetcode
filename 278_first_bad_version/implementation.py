class Solution:

    def __init__(self, bad_version):
        self.bad_version = bad_version

    def isBadVersion(self, i):
        return i >= self.bad_version

    def firstBadVersion(self, n):
        from collections import defaultdict

        lower_index = 0
        upper_index = n
        visited = defaultdict(lambda:True)
        
        while lower_index <= upper_index:

            inspect_index = (upper_index+lower_index) // 2
            inspect_value = self.isBadVersion(inspect_index)
            visited[inspect_index] = inspect_value
            
            print(lower_index, upper_index, inspect_index, inspect_value)

            if inspect_value and not visited[inspect_index-1]:
                return inspect_index
            elif inspect_value:
                upper_index = inspect_index
            else:
                lower_index = inspect_index + 1

        return -1