# https://leetcode.com/problems/add-binary/description/?envType=daily-question&envId=2026-02-15


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ba, bb = int(a, 2), int(b, 2)
        return bin(ba + bb)[2:]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("11", "1"),
        ("1010", "1011"),
    ]

    for a, b in tests:
        res = sol.addBinary(a, b)
        print(res)