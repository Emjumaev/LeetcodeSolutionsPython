class Solution:
    def trap(self, height: List[int]) -> int:
        leftSum = []
        cur = 0
        for i in height:
            leftSum.append(cur)
            cur = max(cur, i)

        rightSum = []
        cur = 0
        for i in height[::-1]:
            rightSum.append(cur)
            cur = max(cur, i)
        rightSum = rightSum[::-1]

        res = 0
        for i in range(len(height)):
            minVal = min(leftSum[i], rightSum[i])
            if minVal > height[i]:
                res += minVal - height[i]

        return res
