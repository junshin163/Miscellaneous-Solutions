class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        firstRow = False
        firstCol = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstRow = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstCol = True
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        for i in range(len(matrix[0])):
            if firstRow:
                matrix[0][i] = 0
        for i in range(len(matrix)):
            if firstCol:
                matrix[i][0] = 0
