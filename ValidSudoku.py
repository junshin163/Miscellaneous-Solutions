class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in rows[r]:
                        return False
                    else:
                        rows[r].add(val)
                    if val in cols[c]:
                        return False
                    else:
                        cols[c].add(val)
                    if val in boxes[(r//3)*3+(c//3)]:
                        return False
                    else:
                        boxes[(r//3)*3+(c//3)].add(val)
        return True
