class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        '''# top-down approach (still time limit exceeded after 44/62 test cases but better than no cache at all)
        cache = [[-1]*(len(nums)) for i in range(len(multipliers))]
        def dp(i, left):
            if i == len(multipliers):
                return 0
            n = len(nums)
            right = n - 1 - (i - left)
            if cache[i][left] == -1:
                cache[i][left] = max(nums[left]*multipliers[i] + dp(i+1, left+1), 
                       nums[right]*multipliers[i] + dp(i+1, left) )         
            return cache[i][left]
        return dp(0, 0)'''
        
        # bottome-up approach:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                mult = multipliers[i]
                dp[i][left] = max(nums[left]*mult+dp[i+1][left+1],
                                                     nums[right]*mult+dp[i+1][left])
        return dp[0][0]
