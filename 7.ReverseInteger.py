# https://leetcode.com/problems/reverse-integer/description/

MIN_INT = -2 ** 31
MAX_INT =  2 ** 31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        start = 0
        str_x = str(x)
        if len(str_x) == 1:
            return x
        if str_x[0] == "-":
            sign = -1
            start = 1 
        rev_str_x = str_x[start::][::-1]
        stripped_x = rev_str_x.lstrip("0")
        num = sign * int(stripped_x)
        if num < MIN_INT or num > MAX_INT:
            return 0
        return num
    
class BestSolution:
    def reverse(self, x: int) -> int:
        res = str(abs(x))
        res = res[::-1]
        res = int(res)

        if x < 0:
            res = -res

        if -2 ** 31 < res < 2 ** 31 - 1:
            return res
        return 0
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        1563847412,
        123,
        -123,
        120,
        0,
        1,
        2,
        7,
    ]

    for test in tests:
        print(sol.reverse(test))