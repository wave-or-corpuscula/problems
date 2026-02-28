# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/?envType=daily-question&envId=2026-02-28

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = [bin(i)[2:] for i in range(1, n + 1)]
        number = int("".join(result), 2) % (10 ** 9 + 7)
        return number

if __name__ == "__main__":
    sol = Solution()

    tests = [
        1, 3, 12
    ]

    for n in tests:
        print(sol.concatenatedBinary(n))