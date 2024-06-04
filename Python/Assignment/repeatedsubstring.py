#Question Repeated substrings

#Code

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0,len(s)):
            check = s[:(i+1)]
            if len(s) % (i + 1) == 0 and len(s) != (i + 1) :
                if check * (len(s)/(i+1)) == s:
                    return True
                    break
        return False
