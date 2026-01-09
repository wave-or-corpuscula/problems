# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09

from typing import Optional
from collections import deque

from binary import TreeNode, build_tree, print_tree


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        levels = []
        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(None)
            if any(x for x in level):
                levels.append(level)
        for i in range(len(levels) - 1, -1, -1):
            print(levels[i])


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [3,5,1,6,2,0,8,None,None,7,4],
        [1],
        [0,1,3,None,2],
    ]

    for test in tests:
        tree = build_tree(test)
        print_tree(tree)

        res = sol.subtreeWithAllDeepest(tree)
        print(res)