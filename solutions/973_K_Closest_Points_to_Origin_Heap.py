import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            minHeap.append([dist, point[0], point[1]])

        heapq.heapify(minHeap)
        res = []

        while(k > 0):
            arr = heapq.heappop(minHeap)
            res.append([arr[1], arr[2]])
            k -= 1

        return res
