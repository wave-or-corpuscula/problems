# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/?envType=daily-question&envId=2026-02-27

from math import inf


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        
        if n == k:
            if z == 0:
                return 0
            elif z == n:
                return 1
            else:
                return -1
        
        def ceil(x, y):
            return (x + y - 1) // y
        
        ans = inf
        
        if z % 2 == 0:
            m = max(ceil(z, k), ceil(z, n - k))
            if m % 2 == 1:
                m += 1
            ans = min(ans, m)
        
        if z % 2 == k % 2:
            m = max(ceil(z, k), ceil(n - z, n - k))
            if m % 2 == 0:
                m += 1
            ans = min(ans, m)
        
        return ans if ans < inf else -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("110",  1),
        ("0101", 3),
        ("101",  2)
    ]
    for s, k in tests:
        res = sol.minOperations(s, k)
        print(res)