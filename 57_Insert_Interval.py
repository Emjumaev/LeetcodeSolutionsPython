class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for current in intervals:
            if current[0] < newInterval[0]:
                if current[1] >= newInterval[0]:
                    # merge two intervals
                    newInterval = self.merge(current, newInterval)
                else:
                    res.append(current)
            elif current[0] > newInterval[0]:
                if current[0] <= newInterval[1]:
                    # merge
                    newInterval = self.merge(current, newInterval)
                else:
                    res.append(current)
            else:
                # merge
                newInterval = self.merge(current, newInterval)

        res.append(newInterval)
        res.sort(key=lambda x: x[0])

        return res

    def merge(self, interval1: [int], interval2: [int]) -> [int]:
        newInterval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        return newInterval
