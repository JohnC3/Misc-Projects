# https://leetcode.com/problems/spiral-matrix-ii/description/

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


"""
4
16
[
[1, 2, 3, 4],
[12, 13, 14, 5],
[11, 16, 15, 6],
[10, 9, 8, 7]
]
"""

# class Node(object):
#
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# class single_linked_list(self):
#
#     def __init__(self):
#         fake_head = Node(None)
#         self.empty = True
#         self.head = fake_head
#         self.tail = fake_head
#
#     def append(self, new_node):
#         if self.empty:
#             self.head = new_node
#             self.empty = False
#         self.tail.next = new_node
#         self.tail = new_node
#
#     def add(self, new_node, prev_node=None):
#
#         if prev_node is None:
#             self.append(new_node)
#
#         new_node.next = prev_node.next
#
#         prev_node.next = new_node
#
#     def delete(self, del_node, prev_node):
#
#         prev_node.next = del_node.next
#
#         if del_node == self.tail:
#             self.
#


def spiral_generator(n):

    matrix = [['.' for r in range(n)] for c in range(n)]
    print(matrix)

    dirs = [
        ('left', 0, 1),
        ('down', 1, 0),
        ('right', 0, -1),
        ('up', -1, 0)]
    dirs_dex = 0
    name, drow, dcol = dirs[dirs_dex]
    val = 0
    row, col = 0, 0
    while val <= n**2:

        pr, pc = row, col
        matrix[row][col] = val
        row = row + drow
        col = col + dcol

        if row > n - 1 or col > n - 1 or row < 0 or col < 0:
            dirs_dex = (dirs_dex + 1) % 4
            name, drow, dcol = dirs[dirs_dex]
            print('now going ', name)
            row = pr + drow
            col = pc + dcol
            print(row, col)
        elif matrix[row][col] != '.':
            dirs_dex = (dirs_dex + 1) % 4
            name, drow, dcol = dirs[dirs_dex]
            row = pr + drow
            col = pc + dcol
        print('@ {} {}, going {}'.format(row, col, name))

        val += 1
    return matrix

print(spiral_generator(4))
