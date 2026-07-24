class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = []

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            cur = intervals[i]

            # check for intersection
            if prev[1] >= cur[0]:
                intervals[i] = [min(prev[0], cur[0]), max(prev[1], cur[1])]
            else:
                res.append(prev)

        res.append(intervals[-1])

        return res
