class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        self.dfs(nums, [], counter)

        return self.res


    def dfs(self, nums: List[int], permutation: List[int], counter: dict[int, int]):
        if counter == {}:
            self.res.append(permutation.copy())

        for num in set(nums):
            if num in counter:
                counter[num] -= 1

                if counter[num] == 0:
                    counter.pop(num, None)
            else:
                continue
            permutation.append(num)

            self.dfs(nums, permutation, counter)

            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            permutation.pop()
