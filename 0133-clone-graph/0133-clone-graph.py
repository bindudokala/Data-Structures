"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeCopy = {}
        if not node:
            return None

        # using DFS to create copy of each old new and add the new neighbors to the copy using a HashMap
        def dfs(node):
            if node in nodeCopy:
                return nodeCopy[node]
            copy = Node(node.val)
            nodeCopy[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)

