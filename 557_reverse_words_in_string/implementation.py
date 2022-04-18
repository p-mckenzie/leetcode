class Solution:
    def reverseString(self, s):
        length = len(s)

        for i in range(length//2):
            holder = s[i]
            s[i] = s[length - i - 1]
            s[length - i -1] = holder

        return s

    def reverseWords(self, s):
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = ''.join(self.reverseString(list(words[i])))
        return ' '.join(words)