class Solution(object):
    def twoSum(self, nums, target):
        """
        enumerate each pair of elements in nums
        to find out the ans 
        """
        for id1 in range(0,len(nums)-1):
            for id2 in range(id1+1,len(nums)):
                if(nums[id1]+nums[id2]==target):
                    return [id1,id2]