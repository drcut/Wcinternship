class Solution(object):
    def reverseWords(self, s):
        """
        reverse string s
        """
        return ' '.join(list(reversed(s.split())))