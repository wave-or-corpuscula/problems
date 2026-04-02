# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1


        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[-1]
    

class ConstSpaceSolution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1
        a,b,c = 0, 1, 1
        for _ in range(3, n + 1):
            s = a + b + c
            a = b
            b = c
            c = s
        return s