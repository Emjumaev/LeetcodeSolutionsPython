"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = []
        endTimes = []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)

        startTimes.sort()
        endTimes.sort()

        i, j = 0, 0
        n = len(intervals)
        count = 0
        res = 0

        while(i < n and j < n):
            if startTimes[i] < endTimes[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1

            res = max(res, count)

        return res
