# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=dsa-association-slope-linked-list

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head.next
        prev = head

        while True:
            while cur and prev.val == cur.val:
                cur = cur.next
            if not cur:
                prev.next = None
                break
            prev.next = cur
            prev = cur
            cur = cur.next

        return head


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,1,2],
        [1,1,2,3,3],
    ]

    for h in tests:
        llist = llist_make(h)
        llist_print(llist)
        res = sol.deleteDuplicates(llist)
        llist_print(res)