# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        while list1 or list2:
            if list1 and list2:
                big_node = list1
                lil_node = list2
                if big_node > lil_node:
                    big_node, lil_node = lil_node, big_node
                root.next = 