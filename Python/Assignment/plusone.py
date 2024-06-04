#Question Add one to the last number of array and display the result

#Code

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        j=len(digits)
        for i in range(j-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits

        digits.insert(0,1)
        return digits  
