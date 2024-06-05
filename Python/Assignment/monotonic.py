#Question Monotonic array

#Code

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = False
        n = False
        count = 0
        for i in range(0,len(nums) - 1):
            if nums[i] < nums[i+1]:
                m = True
                count = i + 1
                break
            if nums[i] > nums[i+1]:
                n = True
                count = i + 1
                break
        if (not m) and (not n):
            return True
        for j in range(count,len(nums) - 1):
            if m and nums[j] > nums[j+1]:
                return False
                break
            if n  and nums[j] < nums[j+1]:
                return False
                break
        return True
        
