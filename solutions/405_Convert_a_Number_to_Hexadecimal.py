class Solution:
    def toHex(self, num: int) -> str:
        hex = ""

        if num == 0:
            return "0"

        num &= 0xFFFFFFFF

        while(num > 0):
            mod = num % 16
            match mod:
                case 10:
                    hex += "a"
                case 11:
                    hex += "b"
                case 12:
                    hex += "c"
                case 13:
                    hex += "d"
                case 14:
                    hex += "e"
                case 15:
                    hex += "f"
                case _:
                    hex += str(mod)

            num = num // 16

        return hex[::-1]
