class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        self.adjList = {}
        self.visit = set()
        res = 0

        for i in range(n):
            self.adjList[i] = []

        for edge in connections:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])

        for i in range(n):
            if i not in self.visit:
                self.dfs(i, -1, set())
                res += 1

        return res - 1


    def dfs(self, node: int, parent: int, path: set[int]):

        if node in path:
            return

        path.add(node)
        self.visit.add(node)

        for adjacent in self.adjList[node]:
            if adjacent == parent:
                continue

            self.dfs(adjacent, node, path)

        path.remove(node)
        self.adjList[node] = []
        return
