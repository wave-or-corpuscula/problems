# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

import math

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = prev.next
        while cur:
            gcd = ListNode(val=math.gcd(prev.val, cur.val), next=cur)
            prev.next = gcd

            prev = cur
            cur = cur.next
        return head