class Solution(object):
    def maxSubArray(self, nums):
        """
        dp[k] stands for the max sub-array's sum which
         end by kth-element 
        """
        rtype = nums[0]
        dp = []
        dp.append(nums[0])
        for id in range(1,len(nums)):
        	if nums[id] + dp[id-1] > nums[id]:
                dp.append(nums[id] + dp[id-1])
        	else:
                dp.append(nums[id])
        	if(dp[id] > rtype):
                rtype = dp[id]
        return rtype