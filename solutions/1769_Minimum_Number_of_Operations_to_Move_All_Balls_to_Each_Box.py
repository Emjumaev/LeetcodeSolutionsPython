class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        nonEmptyIndices = []
        for (index, box) in enumerate(boxes):
            if box == "1":
                nonEmptyIndices.append(index)

        res = []
        for index, box in enumerate(boxes):
            sum = 0
            for nonEmpty in nonEmptyIndices:
                sum += abs(nonEmpty - index)
            res.append(sum)

        return res
