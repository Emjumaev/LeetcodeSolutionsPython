class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                res = 0
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if token == "+":
                    res = num2 + num1
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num2 * num1
                elif token == "/":
                    res = int(num2 / num1)

                stack.append(res)
            else:
                stack.append(token)

        return int(stack[0])
