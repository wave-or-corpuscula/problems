# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/?envType=daily-question&envId=2026-02-24

from typing import Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, root.val)]
        to_leaf_sum = 0
        while stack:
            node, path = stack.pop()

            if node.left is None and node.right is None:
                to_leaf_sum += path

            if node.left:
                stack.append((node.left, (path << 1) + node.left.val))
            if node.right:
                stack.append((node.right, (path << 1) + node.right.val))
        
        return to_leaf_sum