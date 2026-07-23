class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.adjList = {}

        for i in range(0, n):
            self.adjList[i] = []

        for edge in edges:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])

        print(self.adjList)

        return self.dfs(-1, source, destination, set())

    def dfs(self, parent: int, src: int, dest: int, hashSet: set[int]) -> Bool:
        if parent == src:
            return False

        if dest == src:
            return True

        for neighbor in self.adjList[src]:
            if neighbor in hashSet:
                continue

            hashSet.add(neighbor)
            if self.dfs(src, neighbor, dest, hashSet):
                return True
        return False
