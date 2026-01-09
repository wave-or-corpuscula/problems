# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09

from typing import Optional
from collections import deque

from binary import TreeNode, build_tree, print_tree


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> TreeNode:
            if not node: return (None, 0)
            l_node, l_dist = dfs(node.left)
            r_node, r_dist = dfs(node.right)

            if l_dist > r_dist:
                return (l_node, l_dist + 1)
            elif r_dist > l_dist:
                return (r_node, r_dist + 1)
            else:
                return (node, l_dist + 1)
        return dfs(root)[0]
        
# TODO: Разобрать задачу

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