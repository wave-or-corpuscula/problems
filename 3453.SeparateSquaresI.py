# https://leetcode.com/problems/separate-squares-i/description/?envType=daily-question&envId=2026-01-13

import random
from typing import List

import matplotlib.pyplot as plt

colors = [ 'crimson', 'dodgerblue', 'limegreen', 'black']


def draw_squares(squares: List[List[int]]):
    for x, y, side in squares:
        col = random.choice(colors)
        plt.plot([x, x + side, x + side, x, x],
                 [y, y, y + side, y + side, y],
                 color=col, linestyle='solid')
    plt.gca().set_aspect('equal')
    plt.show()
        

# def area_below_y(squares: List[List[int]], dy: float):
#     area = 0
#     for _, y, side in squares:
#         if dy <= y:
#             continue
#         elif dy >= y + side:
#             area += side ** 2
#         else:
#             area += (dy - y) * side
#     return area



class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        def area_below_y(dy: float):
            area = 0
            for _, y, side in squares:
                if dy <= y:
                    continue
                elif dy >= y + side:
                    area += side * side
                else:
                    area += (dy - y) * side
            return area

        right = max(y + side for _, y, side in squares)
        left = min(y for _, y, _ in squares)
        target_area = area_below_y(right) / 2

        print(f"({left, right}), {target_area}")
        while (right - left) > 1e-6:
            mid = (right + left) / 2
            area = area_below_y(mid)

            if area < target_area:
                left = mid
            else:
                right = mid
        return left

# TODO: Порешать задачки на бинарный поиск (закрепить тему)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [[0,0,1],[2,2,1]],
        [[0,0,1],[1,1,2], [3, 3, 3], [6, 6, 6], [5, 5, 5]],
        [[0,0,2],[1,1,1]],
    ]

    for test in tests:
        draw_squares(test)
        res = sol.separateSquares(test)
        print(f"Result: {res}")

