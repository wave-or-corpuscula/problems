# https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        target_set = set(target)
        l = len(target)
        elements_count = 0
        
        for i in range(1, n + 1):
            stack.append("Push")

            if i in target_set:
                elements_count += 1
            else:
                stack.append("Push")
            if elements_count == l:
                break
        return stack


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,3], 3),
        ([1,2,3], 3),
        ([1,2], 4),
    ]

    for target, n in tests:
        res = sol.buildArray(target, n)
        print(res)