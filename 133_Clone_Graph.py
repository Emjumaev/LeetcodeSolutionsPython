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
        if node == None:
            return None

        self.oldToNew = {}

        return self.dfs(node)

    def dfs(self, node: Optional['Node']) -> Optional['Node']:

        if node in self.oldToNew:
            return self.oldToNew[node]

        copy = Node(node.val)
        self.oldToNew[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor))

        return copy
