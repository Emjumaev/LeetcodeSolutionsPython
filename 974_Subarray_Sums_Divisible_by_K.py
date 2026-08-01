class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixArr = []
        res = 0
        curSum = 0

        # Compute prefix sums modulo k
        for num in nums:
            curSum += num
            prefixArr.append(curSum % k)

        # Count occurrences of each remainder
        counter = {0: 1}

        for rem in prefixArr:
            if rem in counter:
                res += counter[rem]
                counter[rem] += 1
            else:
                counter[rem] = 1

        return res
