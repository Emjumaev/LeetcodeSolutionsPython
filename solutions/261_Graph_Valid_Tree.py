class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adjList = {}
        self.visit = set()

        for i in range(n):
            self.adjList[i] = []

        for edge in edges:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])

        if self.checkForCycle(0, -1):
            return False

        # did we visit all the nodes
        for i in range(n):
            if i not in self.visit:
                return False

        return True


    def checkForCycle(self, node: int, parent) -> bool:
        if node in self.visit:
            return True

        self.visit.add(node)

        for adjecent in self.adjList[node]:
            if parent == adjecent:
                continue
            if self.checkForCycle(adjecent, node):
                return True

        return False
