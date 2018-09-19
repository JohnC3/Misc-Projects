# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root.left is None and root.right is None:
            return 1

        if root.left:
            my_left = self.maxDepth(root.left)

        else:
            my_left = 0

        print(root.left.val, my_left)

        if root.right:
            my_right = self.maxDepth(root.right)
        else:
            my_right = 0
        print(root.right, my_right)

        my_height = max(my_left, my_right) + 1
        print('val, height', root.val, my_height)

        return max(my_left, my_right) + 1

root = TreeNode(3)

root.left = TreeNode(9)
root.left.left = None
root.left.right = None

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.maxDepth(root)
