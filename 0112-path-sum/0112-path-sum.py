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
        def dfs(node, pathSum):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return pathSum + node.val == targetSum
            return dfs(node.left, pathSum + node.val) or dfs(node.right, pathSum + node.val) 
        return dfs(root, pathSum)