# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maximum = float("-inf")

        def dfs(node):

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current_sum = node.val + left + right

            self.maximum = max(self.maximum, current_sum)

            return node.val + max(left, right)

        dfs(root)

        return self.maximum
        