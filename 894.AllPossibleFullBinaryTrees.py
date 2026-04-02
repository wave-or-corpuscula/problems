# https://leetcode.com/problems/all-possible-full-binary-trees/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

memo = {}

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        if n in memo:
            return memo[n]
        
        res = []
        for i in range(1, n, 2):
            left_trees = self.allPossibleFBT(i)
            right_trees = self.allPossibleFBT(n - 1 - i)

            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
        memo[n] = res

        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        7, 3
    ]

    for n in tests:
        res = sol.allPossibleFBT(n)
        print(res)
        