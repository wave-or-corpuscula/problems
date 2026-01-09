# https://leetcode.com/problems/same-tree/

from typing import Optional, List

from binary import TreeNode, build_tree, print_tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def flatten_tree(node: Optional[TreeNode]) -> List:
            if not node:
                return [None]
            return [node.val] + flatten_tree(node.left) + flatten_tree(node.right)
        
        return flatten_tree(p) == flatten_tree(q)
        


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,2,3], [1,2,3]),
        ([1,2], [1,None,2]),
        ([1,2,1], [1,1,2]),
    ]

    for test in tests:
        print("New test")
        p, q = test
        p_tree = build_tree(p)
        q_tree = build_tree(q)

        print_tree(p_tree)
        print_tree(q_tree)

        res = sol.isSameTree(p_tree, q_tree)
        print(res)