# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20

from typing import List


class BrutForceSolution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)

        best = 0
        for i in range(N - 1):
            for j in range(N - 1, i, -1):
                if colors[i] != colors[j]:
                    best = max(best, j - i)
                    break
        return best


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)

        best = 0
        for i in range(N):
            if colors[i] != colors[-1]:
                best = max(best, N - i - 1)
                break

        for i in range(N - 1, -1, -1):
            if colors[i] != colors[0]:
                best = max(best, i)
                break

        return best
        


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,1,1,6,1,1,1],
        [1,8,3,8,3],
        [0,1],
    ]

    for col in tests:
        res = sol.maxDistance(col)
        print(res)
    