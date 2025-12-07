# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS - adding node values from the root to the leaf nodes - top to bottom path sum check
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0
        def dfs(self, node, pathSum):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return pathSum + node.val == targetSum
            return dfs(self, node.left, node.val + pathSum) or dfs(self, node.right, node.val + pathSum) 
        return dfs(self, root, pathSum)