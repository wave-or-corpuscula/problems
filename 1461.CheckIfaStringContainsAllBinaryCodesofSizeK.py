# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N = len(s)
        seen = {s[i: i + k] for i in range(N - k + 1)}
        return len(seen) == 2 ** k


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("00110110", 2),
        ("0110", 1),
        ("0110", 2),
    ]
    for s, k in tests:
        res = sol.hasAllCodes(s, k)
        print(res)