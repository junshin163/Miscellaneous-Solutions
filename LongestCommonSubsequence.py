class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """ 
        # bottom-up tabulation (real dynamic programming):
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        if text1[m-1] == text2[n-1]:
            dp[m-1][n-1] = 1
            
        for i in range(m-1, -1, -1):
            if text1[i] == text2[n-1]:
                dp[i][n-1] = 1
            else:
                curr = i + 1
                while curr < m:
                    if dp[curr][n-1] == 1:
                        dp[i][n-1] = 1
                    curr += 1
                
        for j in range(n-1, -1, -1):
            if text2[j] == text1[m-1]:
                dp[m-1][j] = 1
            else:
                curr = j + 1
                while curr < n:
                    if dp[m-1][curr] == 1:
                        dp[m-1][j] = 1
                    curr += 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)
        return dp[0][0]
