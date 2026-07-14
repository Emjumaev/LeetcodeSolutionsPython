class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = ""

        while(i >= 0 or j >= 0):
            if i < 0:
                val1 = 0
            else:
                val1 = int(a[i])

            if j < 0:
                val2 = 0
            else:
                val2 = int(b[j])

            sum = val1 + val2 + carry
            carry = sum // 2
            res = str(sum % 2) + res

            i -= 1
            j -= 1

        if carry == 1:
            res = "1" + res

        return res
