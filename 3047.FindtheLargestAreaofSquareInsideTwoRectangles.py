# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/?envType=daily-question&envId=2026-01-17

from typing import List


class BrutforceSolution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        n = len(bottomLeft)
        
        def overlap(a: int, b: int, c: int, d: int) -> int:
            return max(min(b, d) - max(a, c), 0)

        def intersect_area(i: int, j: int) -> int:
            (ax, ay), (bx, by) = bottomLeft[i], topRight[i]
            (cx, cy), (dx, dy) = bottomLeft[j], topRight[j]

            overlapx = overlap(ax, bx, cx, dx)
            overlapy = overlap(ay, by, cy, dy)
            
            return min(overlapx, overlapy) ** 2 
        
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                best = max(best, intersect_area(i, j))
        return best


if __name__ == "__main__":
    sol = BrutforceSolution()
    tests = [
        ([[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]]),
        ([[1,1],[2,2],[1,2]], [[3,3],[4,4],[3,4]]),
        ([[1,1],[3,3],[3,1]], [[2,2],[4,4],[4,2]]),
    ]
    for bl, tr in tests:
        res = sol.largestSquareArea(bl, tr)
        print(res)