class Solution(object):
    def majorityElement(self, nums):
        """
        a majority element must be the middle in a sorted array
        """
        nums.sort()
        return nums[len(nums)/2]