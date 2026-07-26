class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # building adjacency List
        self.adjList = {}
        self.res = []
        self.visit = set()

        for i in range(numCourses):
            self.adjList[i] = []

        for prerequisite in prerequisites:
            self.adjList[prerequisite[0]].append(prerequisite[1])

        # checking for cycle detection in every node
        for i in range(numCourses):
            if self.checkForCycle(i, set()):
                return []

        return self.res

    # cycle detection
    def checkForCycle(self, node: int, path: set[int]) -> bool:
        if node in path:
            return True

        path.add(node)

        for adjecent in self.adjList[node]:
            if self.checkForCycle(adjecent, path):
                path.remove(node)
                return True

        path.remove(node)
        self.adjList[node] = []

        if node not in self.visit:
            self.res.append(node)
            self.visit.add(node)
        return False
