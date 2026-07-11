class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left = 0
        right = 1
        res = 0

        while(right < len(prices)):
            res = max(res, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left += 1
            else:
                right += 1

        return res
