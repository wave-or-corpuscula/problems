# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

from typing import List




class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def apply(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "/":
                return int(a/b)
            else:
                return a * b
        
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operations:
                second = stack.pop()
                first = stack.pop()
                result = apply(first, second, token)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ["4","-2","/","2","-3","-","-"], # -7
        ["114","-112","*"],
        ["18"],
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ]

    for test in tests:
        res = sol.evalRPN(test)
        print(res)