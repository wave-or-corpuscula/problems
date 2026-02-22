# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-21


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_cnt = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for x in range(left, right + 1, 1):
            
            # ons_cnt = 0
            # while x:
            #     if x & 1:
            #         ons_cnt += 1
            #     x >>= 1
            
            ons_cnt = bin(x).count('1')
            if ons_cnt in primes:
                prime_cnt += 1
        return prime_cnt


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (6, 10),
        (10, 15)
    ]

    for left, right in tests:
        res = sol.countPrimeSetBits(left, right)
        print(res)