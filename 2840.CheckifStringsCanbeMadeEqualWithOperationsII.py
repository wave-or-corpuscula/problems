# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/?envType=daily-question&envId=2026-03-30

from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcdba", "cabdab"),
        ("abe",    "bea"),
    ]

for s1, s2 in tests:
    res = sol.checkStrings(s1, s2)
    print(res)