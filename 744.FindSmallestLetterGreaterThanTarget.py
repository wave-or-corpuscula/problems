# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=daily-question&envId=2026-01-31

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        greater_target = [c for c in set(letters) if c > target]
        
        return min(greater_target) if greater_target else letters[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["c","f","j"], "a"),
        (["c","f","j"], "c"),
        (["x","x","y","y"], "z"),
        (["c","f","j"], "d")
    ]

    for letters, target in tests:
        res = sol.nextGreatestLetter(letters, target)
        print(res)