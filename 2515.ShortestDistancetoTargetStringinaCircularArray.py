# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/?envType=daily-question&envId=2026-04-15

from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N = len(words)
        i = 0
        for _ in range(N):
            if words[(i + startIndex) % N] == target or words[-(i - startIndex) % N] == target:
                return i
            i += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["hello","i","am","leetcode","hello"], "hello", 1),
        (["a","b","leetcode"], "leetcode", 0),
        (["i","eat","leetcode"], "ate", 0)
    ]

    for w, tar, si in tests:
        res = sol.closestTarget(w, tar, si)
        print(res)
