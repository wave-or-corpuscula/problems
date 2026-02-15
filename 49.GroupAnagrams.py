# leetcode.com/problems/group-anagrams/description/

from typing import List

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            result["".join(sorted(s))].append(s)
        return [v for v in result.values()]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
    ]

    for strs in tests:
        res = sol.groupAnagrams(strs)
        print(res)