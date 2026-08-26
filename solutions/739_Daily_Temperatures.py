class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []

        for i in range(len(temperatures) - 1, -1, -1):
            item = temperatures[i]

            while(len(stack) != 0 and stack[-1][0] <= item):
                stack.pop(-1)

            if len(stack) == 0:
                ans.append(0)
            else:
                indexOnTop = stack[-1][1]
                ans.append(indexOnTop - i)

            stack.append((item, i))

        return ans[::-1]
