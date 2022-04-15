class Solution:
    def reverseString(self, s):
        length = len(s)

        for i in range(length//2):
            holder = s[i]
            s[i] = s[length - i - 1]
            s[length - i -1] = holder

        return s
