#Question Convert Roman to integer

#Code

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        val=0

        for i in range(len(s)):
            val=val+values[s[i]]
            if i!=0:
                if values[s[i]]>values[s[i-1]]:
                    val=val-2*(values[s[i-1]])
        return val 
