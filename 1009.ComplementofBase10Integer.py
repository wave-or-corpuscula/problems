# https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bn = bin(n)[2:]
        ans = "".join(map(lambda s: '1' if s == '0' else '0', bn))
        return int(ans, 2)


print(Solution().bitwiseComplement(5))