class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = intervals[i - 1]

            if prev[1] > cur[0]:
                if prev[1] < cur[1]:
                    intervals[i] = prev
                else:
                    intervals[i] = cur

                res += 1

        return res
