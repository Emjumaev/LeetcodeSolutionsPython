from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for operation in operations:
            if operation == "C":
                res.pop()
            elif operation == "D":
                res.append(res[-1] * 2)
            elif operation == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(operation))

        return sum(res)
