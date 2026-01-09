# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=daily-question&envId=2026-01-05

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + low % 2
    
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, 7),  # 7  - 3 = 4 [3, (4, 5, 6,) 7]
        (8, 10), # 10 - 8 = 2 [8, (9,) 10]
        (4, 11), # 11 - 4 = 7 [4, (5, 6, 7, 8, 9, 10,) 11]
        (3, 6),  # 6  - 3 = 3 [3, (4, 5,) 6]
    ]

    for test in tests:
        res = sol.countOdds(*test)
        print(res)