# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "1001",
        "110"
    ]

    for s in tests:
        res = sol.checkOnesSegment(s)
        print(res)