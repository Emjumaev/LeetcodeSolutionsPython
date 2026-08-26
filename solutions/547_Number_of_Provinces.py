class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adjList = {}
        self.visit = set()
        res = 0
        n = len(isConnected)

        for i in range(n):
            self.adjList[i] = []


        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    self.adjList[i].append(j)

        print(self.adjList)
        for i in range(n):
            if i not in self.visit:
                self.dfs(i, -1, set())
                res += 1

        return res


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
