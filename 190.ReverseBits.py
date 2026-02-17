# https://leetcode.com/problems/reverse-bits/description/?envType=daily-question&envId=2026-02-16

class Solution:
    def reverseBits(self, n: int) -> int:
        bn = bin(n)[2:]
        full_bn = bn.zfill(32)
        return int(full_bn[::-1], 2)


class BetterSolution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n & (1<<i):
                ans += 2 ** (31 - i)
        return ans
