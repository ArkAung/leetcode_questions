# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        leaves2 = []

        def dfs(node, tree):
            nonlocal leaves1, leaves2
            if node is None:
                return
            if node.left is None and node.right is None:
                if tree == 1:
                    leaves1.append(node.val)
                else:
                    leaves2.append(node.val)
            dfs(node.left, tree)
            dfs(node.right, tree)

        dfs(root1, tree=1)
        dfs(root2, tree=2)

        return leaves1 == leaves2
