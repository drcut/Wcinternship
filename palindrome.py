class Solution(object):
    def isPalindrome(self, s):
        """
        figure out if s is a Palindrome with taking only 
        letter and digit into account
        clear_s stand for the letter and digit 
        of s with the same order
        """
        clear_s = [x for x in s if x.isalpha() or x.isdigit()]
        """
        if s is empty,we think it is a Palindrome
        """
        if not clear_s:
            return True
        for c1, c2 in zip(clear_s,list(reversed(clear_s))):
            if(c1.lower() != c2.lower()):
                return False
        return True