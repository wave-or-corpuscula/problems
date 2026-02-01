# https://leetcode.com/problems/maximum-substrings-with-distinct-start/description/


class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))