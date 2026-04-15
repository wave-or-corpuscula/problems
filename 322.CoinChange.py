# https://leetcode.com/problems/coin-change/description/

from math import inf
from typing import List
from collections import deque


class BFSSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
                    0
            1       2       5
          1 2 5   1 2 5   1 2 5
        
        
        """
        if amount == 0:
            return 0
        
        queue = deque([(0, 0)])
        visited = set()

        while queue:
            current_sum, level = queue.popleft()
            if current_sum == amount:
                return level
            
            if current_sum in visited or current_sum > amount:
                continue

            visited.add(current_sum)
            for coin in coins:
                queue.append((current_sum + coin, level + 1))
        return -1
    

class DPSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] is inf else dp[amount]




if __name__ == "__main__":
    sol = DPSolution()
    tests = [
        ([10], 10),
        ([1,2,5], 11),
        ([2], 3),
        ([1], 0),
    ]

    for coins, amount in tests:
        res = sol.coinChange(coins, amount)
        print(res)