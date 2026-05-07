# https://leetcode.com/problems/coin-change-ii/description/

from collections import deque
from math import inf
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        return dp[amount]
        


