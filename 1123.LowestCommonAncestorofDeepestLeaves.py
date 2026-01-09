# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

from binary import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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