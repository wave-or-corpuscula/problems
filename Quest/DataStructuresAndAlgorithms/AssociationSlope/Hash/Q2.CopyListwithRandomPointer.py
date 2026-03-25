# 

from typing import Optional, List



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        return f"Node(x: {self.val}, next: {self.next}, random: {self.random})"


def llist_make(l: List[List[int | None]]) -> Optional[Node]:
    x, rand = l[0]
    head = Node(x=x)
    current = head
    nodes_map = {x: head}
    for i in range(1, len(l)):
        x, rand = l[i]
        current.next = Node(x=x, random=rand)
        current = current.next
        if rand:
            nodes_map[i] = current
    current = head
    while current:
        if current.random:
            current.random = nodes_map[current.random]
        current = current.next

    return head

def llist_print(head: Optional[Node]):
    cur = head
    while cur:
        print(cur, end=" ")
        cur = cur.next
    print()


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[7,None],[13,0],[11,4],[10,2],[1,0]],
        [[1,1],[2,1]],
        [[3,None],[3,0],[3,None]],
    ]

    for h in tests:
        head = llist_make(h)
        llist_print(head)
        # res = sol.copyRandomList()
        # print(res)