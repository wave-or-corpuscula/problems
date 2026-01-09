# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/?envType=daily-question&envId=2026-01-03

class Solution:
    def numOfWays(self, n: int) -> int:
        dpA = 6  # AAA
        dpB = 6  # ABA
        
        for _ in range(2, n + 1):
            newA = (dpA * 2 + dpB * 2)
            newB = (dpA * 2 + dpB * 3)
            print(dpA, dpB)
            dpA, dpB = newA, newB
        
        return (dpA + dpB) % (10**9 + 7)
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # 1,
        10,
        # 5000
    ]
    for test in tests:
        print(sol.numOfWays(test))