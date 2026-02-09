# https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=daily-question&envId=2026-02-09


from typing import Optional


from binary import TreeNode, build_tree, print_tree



class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_flatten(node: Optional[TreeNode]) -> list[TreeNode]:
            result = []
            if node:
                result += inorder_flatten(node.left)
                result.append(node.val)
                result += inorder_flatten(node.right)
            return result
        
        def sorted_list_to_bst(nums: list[int]):
            if not nums:
                return None
            
            mid = len(nums) // 2
            r = TreeNode(nums[mid])

            r.left = sorted_list_to_bst(nums[:mid])
            r.right = sorted_list_to_bst(nums[mid + 1:])
        
            return r

        tree_arr = inorder_flatten(root)
        balanced_tree = sorted_list_to_bst(tree_arr)
        return balanced_tree


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,None,2,None,3,None,4,None,None],
        [2,1,3],
    ]

    for root in tests:
        tree_root = build_tree(root)
        res = sol.balanceBST(tree_root)
        print_tree(res)
        # print(res)