# https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19

from itertools import pairwise


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cons_lengths = [0]
        prev = s[0]
        for c in s:
            current = c
            if current != prev:
                cons_lengths.append(0)
            cons_lengths[-1] += 1
            prev = current
        
        return sum(min(p1, p2) for p1, p2 in pairwise(cons_lengths))

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "00110011",
        "10101",
    ]

    for s in tests:
        res = sol.countBinarySubstrings(s)
        print(res)