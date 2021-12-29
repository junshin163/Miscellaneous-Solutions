class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 1 or len(matrix[0]) == 1:
            if len(matrix) == 1 and len(matrix[0]) == 1:
                if matrix[0][0] == "1":
                    return 1
                return 0
            elif len(matrix) == 1 and len(matrix[0]) != 1:
                for j in range(len(matrix[0])):
                    if matrix[0][j] == "1":
                        return 1
                return 0
            elif len(matrix) != 1 and len(matrix[0]) == 1:
                for i in range(len(matrix)):
                    if matrix[i][0] == "1":
                        return 1
                return 0
        
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                
        for j in range(len(matrix[0])):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        currLargestSide = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j] > currLargestSide:
                    currLargestSide = dp[i][j]
        return currLargestSide ** 2
