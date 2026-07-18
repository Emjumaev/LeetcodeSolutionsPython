class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        window_sum = sum(arr[:k])

        i = 0
        j = k - 1

        while j < len(arr):
            if window_sum / k >= threshold:
                res += 1

            i += 1
            j += 1

            if j < len(arr):
                window_sum -= arr[i - 1]
                window_sum += arr[j]

        return res
