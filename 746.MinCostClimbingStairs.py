# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 1)
        dp[1] = cost[0]

        for i in range(2, N + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]
        
        return min(dp[-1], dp[-2])
    

class ConstSpaceSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = 0
        f2 = 0

        for i in range(2, len(cost) + 1):
            current = min(f1 + cost[i - 2], f2 + cost[i - 1])

            f1, f2 = f2, current
            
            
        return f2
        


if __name__ == "__main__":
    sol = ConstSpaceSolution()
    tests = [
        [10,15,20],
        [1,100,1,1,1,100,1,1,100,1]
    ]

    for cost in tests:
        res = sol.minCostClimbingStairs(cost)
        print(res)
