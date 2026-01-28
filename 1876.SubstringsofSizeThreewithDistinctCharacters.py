# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/?envType=problem-list-v2&envId=sliding-window

from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sublen = 3
        N = len(s)
        result = 0

        for i in range(0, N - sublen + 1):
            if len(set(s[i:i + sublen])) < sublen:
                continue
            result += 1
            
        return result




if __name__ == "__main__":
    sol = Solution()
    tests = [
        "xyzzaz",
        "aababcabc",
    ]

    for s in tests:
         res = sol.countGoodSubstrings(s)
         print(res)