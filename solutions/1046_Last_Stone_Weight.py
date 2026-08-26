import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            maxHeap.append(-stone)

        heapq.heapify(maxHeap)

        while(len(maxHeap) > 1):
            y = -maxHeap[0]
            heapq.heappop(maxHeap)
            x = -maxHeap[0]
            heapq.heappop(maxHeap)
            if y != x:
                heapq.heappush(maxHeap, x - y)

        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0]
