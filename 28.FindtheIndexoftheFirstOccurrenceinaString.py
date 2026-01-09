# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
    ]

    for test in tests:
        res = sol.strStr(*test)
        print(res)