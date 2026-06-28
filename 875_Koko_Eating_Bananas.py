class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        res = right

        while(left <= right):
            mid = (left + right) // 2

            #calculate number of hours
            numOfHours = 0
            for pile in piles:
                numOfHours += math.ceil(pile / mid)

            if numOfHours <= h:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1

        return res
