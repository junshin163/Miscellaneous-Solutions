class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''# top-down approach (recursion+memoization):
        cache = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max( nums[0], nums[1] )
            if i not in cache:
                cache[i] = max( dp(i - 2) + nums[i], dp(i - 1) )
            return cache[i]
        return dp(len(nums) - 1)'''
        
        # bottom-up approach (list and for loops):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums) 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[len(nums)-1]
