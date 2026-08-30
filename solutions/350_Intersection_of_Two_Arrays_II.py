class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = []

        for ind, val in counter1.items():
            if ind in counter2:
                count = min(counter2[ind], counter1[ind])
                while(count > 0):
                    res.append(ind)
                    count -= 1

        return res
