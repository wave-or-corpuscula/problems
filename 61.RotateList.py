# https://leetcode.com/problems/rotate-list/?envType=daily-question&envId=2026-05-05
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def llist_make(l: list[int]) -> Optional[ListNode]:
    if not l:
        return None
    return ListNode(l[0], llist_make(l[1:]))


def llist_print(node: Optional[ListNode]):
    while node:
        print(node.val, "-> " if node.next else "", end="")
        node = node.next
    print()


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        flatten = []
        while head:
            flatten.append(head.val)
            head = head.next
        
        k %= len(flatten)
        rotated = flatten[-k:] + flatten[:-k]
        head = ListNode()
        dummy = head
        for el in rotated:
            head.next = ListNode(el)
            head = head.next
        
        return dummy.next


class ConstSpaceSolution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        N = 1
        last = head
        while last.next:
            last = last.next
            N += 1

        k %= N
        last.next = head
        
        dummy = head
        for _ in range(N - k - 1):
            dummy = dummy.next

        new_head = dummy.next
        dummy.next = None

        return new_head



if __name__ == "__main__":
    sol = ConstSpaceSolution()
    tests = [
        ([1,2,3,4,5], 2),
        ([0,1,2], 4),
    ]
    for h, k in tests:
        res = sol.rotateRight(llist_make(h), k)
        llist_print(res)