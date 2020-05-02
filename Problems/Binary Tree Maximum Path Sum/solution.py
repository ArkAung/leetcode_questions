# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float("-inf")

        def get_max_path(node):
            nonlocal max_sum
            if node is None:
                return 0

            max_left = max(get_max_path(node.left), 0)
            max_right = max(get_max_path(node.right), 0)

            new_val = node.val + max_left + max_right

            max_sum = max(new_val, max_sum)
            return node.val + max(max_left, max_right)

        get_max_path(root)

        return max_sum