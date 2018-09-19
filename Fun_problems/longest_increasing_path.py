
class Node(object):

    def __init__(self, val):
        self.val
        self.children = []


class Solution:

    def chk_adjacent(self, matrix, row, col):
        n = len(matrix)

        output = []
        # Check left
        if col < n:
            left = matrix[row][col + 1]
            output.append((left, (row, col + 1)))

        if col > 0:
            right = matrix[row][col - 1]
            output.append((right, (row, col - 1)))
        if row < n:
            below = matrix[row + 1][col]
            output.append((below, (row + 1, col)))

        if row > 0:
            above = matrix[row - 1][col]
            output.append((above, (row - 1, col)))

        return output

    def build_tree(self, matrix, row, col, max_val, min_val):

        cur_value = matrix[row][col]

        if min_val >= cur_value or max_val <= cur_value:
            return None


        self.chk_adjacent(matrix, row, col)



    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        n = len(matrix)

        paths = []

        visited = set()

        for row in xrange(n):
            for col in xrange(n):

                self.chk_adjacent(matrix, row, col)


nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
