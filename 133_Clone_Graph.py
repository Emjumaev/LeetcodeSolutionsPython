"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    oldToNew = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None:
            return None

        if node in self.oldToNew:
            return self.oldToNew[node]
        else:
            self.oldToNew[node] = Node(node.val)

        for neighbor in node.neighbors:
            self.oldToNew[node].neighbors.append(self.cloneGraph(neighbor))

        return self.oldToNew[node]
