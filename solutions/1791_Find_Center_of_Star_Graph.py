class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for node in edges[0]:
            if node in edges[1]:
                return node

        return 0
