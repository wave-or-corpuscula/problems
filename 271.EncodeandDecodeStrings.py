# https://leetcode.com/problems/encode-and-decode-strings/description/
# https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

from typing import List


class Solution:

    splitter = "|@|"
    empty = "#mp21@"

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return self.empty
        return self.splitter.join(strs)
        
    def decode(self, s: str) -> List[str]:
        if s is self.empty:
            return []
        if not s:
            return [""]
        return s.split(self.splitter)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ["Hello","World"],
        [""],
        [],
    ]

    for test in tests:
        print(f"Input: {test}")
        encoded = sol.encode(test)
        print(f"Encoded: {encoded}")
        decoded = sol.decode(encoded)
        print(f"Decoded: {decoded}")