# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # DFS - InOrder traversal
        min_diff = [float('inf')]
        prev = [None]
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            if prev[0] is not None:
                min_diff[0] = min(min_diff[0], abs(node.val - prev[0]))
            prev[0] = node.val
            inOrder(node.right)
        inOrder(root)
        return min_diff[0]