# 

from typing import Optional, List



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        return f"\
Node(x: {self.val}, \
next: {self.next.val if self.next else None}, \
random: {f"N({self.random.val})" if isinstance(self.random, Node) else self.random})"


def llist_make(l: List[List[int | None]]) -> Optional[Node]:
    nodes = list(map(lambda args: Node(x=args[0], random=args[1]), l))

    for i in range(1, len(nodes)):
        nodes[i - 1].next = nodes[i]
    
    for i in range(len(nodes)):
        if nodes[i].random is not None:
            nodes[i].random = nodes[nodes[i].random]

    return nodes[0]

def llist_print(head: Optional[Node]):
    cur = head
    while cur:
        print(cur)
        cur = cur.next
    print()


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new.get(curr.next)
            new_node.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[2, None], [7, 3], [11, 3], [15, None], [9, None]]
        # [[7,None],[13,0],[11,4],[10,2],[1,0]],
        # [[1,1],[2,1]],
        # [[3,None],[3,0],[3,None]],
    ]

    for h in tests:
        head = llist_make(h)
        res = sol.copyRandomList(head)
        llist_print(res)