# https://leetcode.com/problems/string-to-integer-atoi/description/

MAX_NUM = 2 ** 31

class Solution:
    def myAtoi(self, s: str) -> int:
        s_no_spaces = s.strip()
        if len(s_no_spaces) == 0:
            return 0
        sign = 1
        start = 0
        if s_no_spaces[0] == "-":
            sign = -1
            start = 1
        elif s_no_spaces[0] == "+":
            start = 1

        end = start
        while end < len(s_no_spaces):
            if not s_no_spaces[end].isdigit():
                break
            end += 1
        int_str = s_no_spaces[start:end]
        if len(int_str) == 0:
            return 0
        num = int(int_str) * sign
        if num > MAX_NUM - 1:
            return MAX_NUM - 1
        elif num < -MAX_NUM:
            return -MAX_NUM
        return num

    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "42",
        " -042",
        "1337c0d3",
        "0-1",
        "00000-42a1234",
        "words and 987",
        "-91283472332",
        "91283472332",
        "-1",
        "2147483648",
    ]

    for test in tests:
        print(f"{test} => {sol.myAtoi(test)}")