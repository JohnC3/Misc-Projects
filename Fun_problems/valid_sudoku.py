# https://leetcode.com/problems/valid-sudoku/description/
class Solution(object):

    def validate_row(self,  arow):
        seen = set()
        for x in arow:
            if x == '.':
                continue
            if x in seen:
                return False
            seen.add(x)
        return True

    def unpack_squares(self, board):
        squares = {}
        for row_dex, row in enumerate(board):
            for col_dex, col in enumerate(row):
                val = board[row_dex][col_dex]
                group = (row_dex // 3, col_dex // 3)
                # print('row_dex, col_dex, group')
                # print(row_dex, col_dex, group)
                if group not in squares:
                    squares[group] = [val]
                else:
                    squares[group].append(val)
        return squares

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        squares = self.unpack_squares(board)

        for row in board:
            if not self.validate_row(row):
                return False

        for s in squares.values():
            if not self.validate_row(s):
                return False

        cols = [r[i] for r in board for i in range(len(board))]
        print(cols)
        for c in cols:
            if not self.validate_row(c):
                return False
        return True


testcase = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

s = Solution()

s.isValidSudoku(testcase)
