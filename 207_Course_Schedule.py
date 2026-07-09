class Solution:
    def __init__(self):
        self.visited = set()
        self.adj_list = {}

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Initialize adjacency list
        for i in range(numCourses):
            self.adj_list[i] = []

        # Build graph
        for course, prereq in prerequisites:
            self.adj_list[course].append(prereq)

        # Check each course
        for course in range(numCourses):
            if not self.dfs(course):
                return False

        return True

    def dfs(self, node: int) -> bool:
        if node in self.visited:
            return False

        self.visited.add(node)

        for neighbor in self.adj_list[node]:
            if not self.dfs(neighbor):
                return False

        self.visited.remove(node)
        self.adj_list[node] = []  # Memoize as already processed

        return True
