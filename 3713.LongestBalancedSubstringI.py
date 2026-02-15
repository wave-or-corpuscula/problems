# https://leetcode.com/problems/longest-balanced-substring-i/description/?envType=daily-question&envId=2026-02-12

from collections import defaultdict


class BrutForceSolution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)
        return res


if __name__ == "__main__":
    sol = BrutForceSolution()
    tests = [
        "zzabccy",
        "a",
        "abbac",
        "aba",
    ]

    for s in tests:
        res = sol.longestBalanced(s)
        print(res)