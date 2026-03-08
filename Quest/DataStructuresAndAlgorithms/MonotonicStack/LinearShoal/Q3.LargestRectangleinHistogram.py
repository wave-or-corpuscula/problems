# https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        best = 0

        for i, h in enumerate(heights):
            area = 0
            j = i
            while j < N and heights[j] >= h:
                area += h
                j += 1
            j = i - 1
            while j >= 0 and heights[j] >= h:
                area += h
                j -= 1
            best = max(best, area)
        return best


class MonotonicStackSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        best = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                ind = stack.pop()
                left = -1 if not stack else stack[-1]
                height = (i - left - 1) * heights[ind]
                best = max(best, height)
            stack.append(i)
        return best



if __name__ == "__main__":
    sol = MonotonicStackSolution()
    tests = [
        [2,1,2],
        [2,1,5,6,2,3],
        [2,4],
    ]

    for heights in tests:
        res = sol.largestRectangleArea(heights)
        print(res)