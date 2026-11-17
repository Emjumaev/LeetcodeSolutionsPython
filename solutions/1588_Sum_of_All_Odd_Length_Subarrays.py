class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            left = i + 1
            right = n - i

            total += arr[i] * ((left * right + 1) // 2)

        return total
