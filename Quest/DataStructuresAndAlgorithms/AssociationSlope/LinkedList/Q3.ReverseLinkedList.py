# https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=dsa-association-slope-linked-list

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val: {self.val}, next: {self.next})"


def llist_make(l: List[int]) -> Optional[ListNode]:
    if not l:
        return None
    head = ListNode(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = ListNode(l[i])
        current = current.next
    return head

def llist_print(head: Optional[ListNode]):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        reversed = ListNode(values[-1])
        current = reversed
        for i in range(len(values) - 2, -1, -1):
            current.next = ListNode(values[i])
            current = current.next
        return reversed


class BetterSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev


if __name__ == "__main__":
    sol = BetterSolution()
    tests = [
        [1,2,3,4,5],
        [1,2],
        []
    ]

    for l in tests:
        llist = llist_make(l)
        res = sol.reverseList(llist)
        llist_print(res)