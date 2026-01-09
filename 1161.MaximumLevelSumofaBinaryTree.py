# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"
    
    def __repr__(self) -> str:
        return f"TreeNode(val: {self.val}, left: {self.left}, right: {self.right})"


def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

def pretty_print_tree(root: TreeNode) -> None:
    if root is None:
        return
    pretty_print_tree(root.left)
    pretty_print_tree(root.right)
    print(root.val)


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


def print_tree_levels(root: TreeNode):
    if not root:
        return
    queue = deque([root])

    max_sum = root.val
    max_level = 0
    cur_level = 0

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if sum(level) > max_sum:
            max_sum = sum(level)
            max_level = cur_level
        cur_level += 1
    return max_level + 1


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = deque([root])

        max_sum = root.val
        max_level = 0
        cur_level = 0

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if any(x is not None for x in level) and sum(level) > max_sum:
                max_sum = sum(level)
                max_level = cur_level
            cur_level += 1
        return max_level + 1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [-100,-200,-300,-20,-5,-10,None],
        [1,7,0,7,-8,None, None],
        # [989,None,10250,98693,-89388,None,None,None,-32127],
        # [1,7,0,7,-8,None,None],
        # [989,None,10250,98693,-89388,None,None,None,-32127],
        # [-100,-200,-300,-20,-5,-10,None],
        # [1,1,0,7,-8,-7,9],
        # [1],
    ]

    for test in tests:
        test_tree = build_tree(test)
        print_tree(test_tree)
        # print(print_tree_levels(test_tree))
        # print()

        res = sol.maxLevelSum(test_tree)
        print(res)
