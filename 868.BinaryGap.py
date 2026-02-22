# https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22


class Solution:
    def binaryGap(self, n: int) -> int:
        
        B = 30
        pos = []
        best = 0
        for i in range(B):
            if (n & (1 << i)):
                pos.append(i)
        for j in range(len(pos) - 1):
            if pos[j + 1] - pos[j] > best:
                best = pos[j + 1] - pos[j]
        return best



if __name__ == "__main__":
    sol = Solution()
    tests = [
        22, 8, 5
    ]

    for n in tests:
        res = sol.binaryGap(n)
        print(res)