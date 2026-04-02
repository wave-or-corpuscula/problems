# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description/?envType=daily-question&envId=2026-04-02

from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        """

        [0,1,-1],
        [1,-2,3],
        [2,-3,4]]
        
        [0,    -inf, -inf], 
        [-inf, -inf, -inf], 
        [-inf, -inf, -inf]]

        [-inf, -inf, -inf], 
        [-inf, -inf, -inf], 
        [-inf, -inf, -inf]

        [-inf, -inf, -inf], 
        [-inf, -inf, -inf], 
        [-inf, -inf, -inf]
        
        
        """
        R, C = len(coins), len(coins[0])
        NEG_INF = float('-inf')

        # dp[i][j][k] — макс. прибыль в (i,j) при k использованных нейтрализациях
        dp = [[[NEG_INF] * 3 for _ in range(C)] for _ in range(R)]

        # База
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # нейтрализовали стартовую клетку

        for i in range(R):
            for j in range(C):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue

                    cell = coins[i][j]

                    # Случай А: не нейтрализуем — берём предшественников с тем же k
                    best = NEG_INF
                    if i > 0 and dp[i-1][j][k] != NEG_INF:
                        best = max(best, dp[i-1][j][k])
                    if j > 0 and dp[i][j-1][k] != NEG_INF:
                        best = max(best, dp[i][j-1][k])

                    if best != NEG_INF:
                        dp[i][j][k] = max(dp[i][j][k], best + cell)

                    # Случай Б: нейтрализуем — берём предшественников с k-1
                    # Проверяем независимо от случая А!
                    if cell < 0 and k >= 1:
                        prev_best = NEG_INF
                        if i > 0 and dp[i-1][j][k-1] != NEG_INF:
                            prev_best = max(prev_best, dp[i-1][j][k-1])
                        if j > 0 and dp[i][j-1][k-1] != NEG_INF:
                            prev_best = max(prev_best, dp[i][j-1][k-1])
                        if prev_best != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], prev_best)

        # Ответ — максимум по всем слоям k в финальной клетке
        return max(dp[R-1][C-1])






if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[0,1,-1],
         [1,-2,3],
         [2,-3,4]],
        # [[10,10,10],
        #  [10,10,10]]
    ]

    for c in tests:
        res = sol.maximumAmount(c)
        print(res)