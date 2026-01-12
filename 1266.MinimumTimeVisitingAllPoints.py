# https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12

from typing import  List

import matplotlib.pyplot as plt
import numpy as np


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(0, len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            time = max((abs(x2 - x1), abs(y2 - y1)))
            total_time += time
            
        return total_time



def draw_points(points: List[List[int]]) -> None:
    xpoints = np.array([p[0] for p in points])
    ypoints = np.array([p[1] for p in points])

    plt.plot(xpoints, ypoints)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [[-3, -2], [2, 4]],
        [[2,-1], [-4,3]],
        [[1,0], [-4,3]],
        [[0, 0], [0, 5], [0, 10]],
        [[0, 10], [0, 5], [0, 0]],
        [[3,1], [3,4], [-1,0]],
        [[1,1], [3,4], [-1,0]],
        [[3,2], [-2,2]],
        [[-2,2],[3,2]],
    ]

    for test in tests:
        # draw_points(test)
        res = sol.minTimeToVisitAllPoints(test)
        print(res)