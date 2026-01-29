# https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2026-01-29

from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        A = 26

        INF = 10 ** 20

        dist = [[INF] * A for _ in range(A)]
        for i in range(A):
            dist[i][i] = 0

        for xc, yc, c in zip(original, changed, cost):
            x = ord(xc) - ord('a')
            y = ord(yc) - ord('a')

            dist[x][y] = min(dist[x][y], c)

        for k in range(A):
            for i in range(A):
                for j in range(A):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        total = 0
        for xc, yc in zip(source, target):
            x = ord(xc) - ord('a')
            y = ord(yc) - ord('a')

            total += dist[x][y]
            if total >= INF:
                return -1
        return total 

        
                



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcd","acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]),
        ("aaaa","bbbb", ["a","c"], ["c","b"], [1,2]),
        ("abcd","abce", ["a"], ["e"], [10000]),
    ]

    for s, t, o, ch, co in tests:
        res = sol.minimumCost(s, t, o, ch, co)
        print(res)