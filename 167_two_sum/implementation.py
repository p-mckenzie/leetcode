class Solution:
    def twoSum(self, numbers, target):

        for i in range(len(numbers)):
            if numbers[i] == numbers[i-1]:
                continue
            goal = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if goal == numbers[j]:
                    return [i+1, j+1]
                elif numbers[j] == numbers[j-1]:
                    continue
                elif numbers[j] > goal:
                    break
