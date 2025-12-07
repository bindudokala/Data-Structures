# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS - perform DFS on the left and right subtrees - go left on one subtree and right on the other subtree to check mirror of subtrees
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        return isMirror(root.left, root.right)