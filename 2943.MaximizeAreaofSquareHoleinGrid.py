# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/?envType=daily-question&envId=2026-01-15

from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hbars = sorted(hBars)
        vbars = sorted(vBars)

        def max_continuous(bars: List[int]) -> int:
            continuous = 1
            max_continuous = 1

            for i in range(1, len(bars)):
                if bars[i] != bars[i - 1] + 1:
                    continuous = 1
                    continue
                continuous += 1
                if continuous > max_continuous:
                    max_continuous = continuous
            return max_continuous

        max_h_cont = max_continuous(hbars)
        max_v_cont = max_continuous(vbars)
        
        return (min(max_h_cont, max_v_cont) + 1) ** 2



if __name__ == "__main__":
    sol = Solution()

    tests = [
        (2, 1, [2,3], [2]),
        (1, 1, [2],   [2]),
        (2, 3, [2,3], [2,4]),
    ]

    for n, m, hbars, vbars in tests:
        res = sol.maximizeSquareHoleArea(n, m, hbars, vbars)
        print(res)