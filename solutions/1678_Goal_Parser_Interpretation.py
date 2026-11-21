class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ""
        while(i < len(command)):
            if command[i] == "G":
                res += command[i]
            elif command[i] == ")" and command[i - 1] == "(":
                res += "o"
            elif command[i] == ")":
                res += "al"
            i += 1
        
        return res
