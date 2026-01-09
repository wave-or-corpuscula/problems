# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n * n < x:
            n += 1
            if n * n > x:
                return n - 1
        return n
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        4,
        8
    ]
    for test in tests:
        print(sol.mySqrt(test))