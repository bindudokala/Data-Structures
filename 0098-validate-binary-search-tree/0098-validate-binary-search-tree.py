# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS - top to bottom approach - for each node on the left, it should be less than the parent which becomes the rightLimit and same for the right side nodes
        def isValidSubtree(root, leftLimit, rightLimit):
            if root is None:
                return True
            if not (leftLimit < root.val < rightLimit):
                return False
            return isValidSubtree(root.left, leftLimit, root.val) and isValidSubtree(root.right, root.val, rightLimit)
            
        return isValidSubtree(root, float('-inf'), float('+inf'))
        