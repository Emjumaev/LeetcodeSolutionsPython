class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        startRange, endRange = nums[0], nums[0]
        self.res = []

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff > 1:
                self.addRangeToRes(startRange, endRange)
                startRange, endRange = nums[i], nums[i]
            else:
                endRange = nums[i]

        self.addRangeToRes(startRange, endRange)

        return self.res

    def addRangeToRes(self, start: int, end: int):
        if start == end:
            self.res.append(f"{end}")
        else:
            self.res.append(f"{start}->{end}")
