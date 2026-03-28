# https://leetcode.com/problems/odd-even-linked-list/?envType=problem-list-v2&envId=dsa-association-slope-linked-list

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val: {self.val}, next: {self.next})"


def llist_make(l: List[int]) -> Optional[ListNode]:
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next:
            return head
        
        odd = head
        even = head.next
        even_start = head.next

        while odd.next and even.next:
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            else:
                odd.next = None
            if even.next.next:
                even.next = even.next.next
                even = even.next
            else:
                even.next = None
        odd.next = even_start
        return head
    
class PrettyerSolution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next:
            return head
        
        odd, even = head, head.next
        even_start = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_start
        return head



if __name__ == "__main__":
    sol = PrettyerSolution()
    tests = [
        [1,2,3,4,5,6],
        [2,1,3,5,6,4,7],
    ]

    for l in tests:
        head = llist_make(l)
        res = sol.oddEvenList(head)
        llist_print(res)
