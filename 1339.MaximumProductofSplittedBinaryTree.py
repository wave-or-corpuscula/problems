# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/?envType=daily-question&envId=2026-01-07

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"


def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # левый потомок
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # правый потомок
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

def print_tree(node, prefix="", is_left=True):
    if not node:
        print(prefix + ("└── " if is_left else "┌── ") + "None")
        return

    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    if node.left or node.right:
        if node.right:
            print_tree(node.right, prefix + ("    " if is_left else "│   "), False)
        else:
            print(prefix + ("    " if is_left else "│   ") + "┌── None")

        if node.left:
            print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        else:
            print(prefix + ("    " if is_left else "│   ") + "└── None")


def tree_sum(root: Optional[TreeNode], subtrees_sums: list) -> int:
    if not root:
        return 0
    subtree_sum = tree_sum(root.left, subtrees_sums) + root.val + tree_sum(root.right, subtrees_sums)
    subtrees_sums.append(subtree_sum)
    return subtree_sum


class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        subtrees_sums = []
        total_sum = tree_sum(root, subtrees_sums)
        return max(map(lambda x: (total_sum - x) * x, subtrees_sums)) % MOD
        # TODO: Посмотреть разные решения и определить, какой подход будет лучше (через массив, через иф в конце)



if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,2,3,4,5,6],
        [1,None,2,3,4,None,None,5,6],
    ]

    for test in tests:
        tree_test = build_tree(test)
        print_tree(tree_test)
        res = sol.maxProduct(tree_test)
        
        print(res)
        # print(tree_sum(tree_test))
