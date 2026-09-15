class Solution:
    def lengthLongestPath(self, input: str) -> int:
        directories = input.split("\n")
        stack = []
        maxDepth = 0

        for directory in directories:
            dirLength = len(directory.split("\t")[-1])
            depthLength = len(directory) - dirLength

            while stack and depthLength <= stack[-1][0]:
                stack.pop()
            
            totalLength = stack[-1][1] + dirLength + 1 if stack else dirLength

            stack.append((depthLength, totalLength))

            if "." in directory:
                maxDepth = max(maxDepth, totalLength)

        return maxDepth
