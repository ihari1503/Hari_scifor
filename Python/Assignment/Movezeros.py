#Question  Move Zeros

#CODE

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        for i in range(0,count):
            nums.remove(0)
        for i in range(0,count):
            nums.append(0)  
