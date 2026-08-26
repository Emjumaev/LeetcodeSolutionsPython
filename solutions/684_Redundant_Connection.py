class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.adjList = {}

        # building adjList
        for edge in edges:
            if edge[0] not in self.adjList:
                self.adjList[edge[0]] = []

            if edge[1] not in self.adjList:
                self.adjList[edge[1]] = []

            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])

        initialSet = set()
        initialSet.add(1)

        self.cycle = []
        self.dfs(0, 1, [1], initialSet)
        print(self.cycle)

        # cycle detection

        print(self.adjList)
        cycleEdges = []

        for i in range(1, len(self.cycle)):
            cycleEdges.append([self.cycle[i - 1], self.cycle[i]])

        for edge in reversed(edges):
            for cycleEdge in cycleEdges:
                if edge[0] == cycleEdge[0] and edge[1] == cycleEdge[1] or edge[1] == cycleEdge[0] and edge[0] == cycleEdge[1]:
                    return edge

        return []


    def dfs(self, parent: int, node: int, path: List[int], hashSet: set[int]) -> bool:
        for neighbor in self.adjList[node]:
            if neighbor == parent:
                continue
            if neighbor in hashSet:
                start_idx = path.index(neighbor)
                self.cycle = path[start_idx:] + [neighbor]
                return True
            path.append(neighbor)
            hashSet.add(neighbor)
            if self.dfs(node, neighbor, path, hashSet):
                return True
            path.pop()
            hashSet.remove(neighbor)

        return False
