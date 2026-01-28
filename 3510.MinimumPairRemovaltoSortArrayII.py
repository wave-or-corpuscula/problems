# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/description/?envType=daily-question&envId=2026-01-23

from typing import List

import heapq


# source: https://stackoverflow.com/questions/79558361/optimizing-leetcodes-minimum-pair-removal-to-sort-array-ii-solution-to-preven

class Node:
    def __init__(self, value, i):
        self.value = value
        self.i = i  # value's index in the original list (to break ties)
        self.prev = self.next = None
        self.descending = False  # True when successor has a smaller value 

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.next = self.prev = None


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) < 2:  # Nothing to do?
            return 0

        # Initialise (heap, doubly linked list, descending-pairs counter)
        heap = []
        num_descending = 0
        node = Node(nums[-1], len(nums) - 1)
        for i in range(len(nums) - 2, -1, -1):
            head = Node(nums[i], i)
            head.next = node
            node.prev = head
            heap.append((head.value + node.value, head.i, head))
            head.descending = head.value > node.value 
            if head.descending:
                num_descending += 1
            node = head

        if num_descending == 0:  # Nothing to do?
            return 0

        heapq.heapify(heap)

        num_operations = 0
        while num_descending > 0:
            value, _, node = heapq.heappop(heap)
            # Value pair is not as expected? (has a member been merged?)
            if not node.next or node.value + node.next.value != value:  
                continue  # Skip this outdated pair
            # Remove next node, and update decreasing-pairs counter accordingly
            if node.next.descending:
                num_descending -= 1
            node.next.remove()

            node.value = value
            num_operations += 1
            # Update heap and number of descending pairs:
            for pair in node.prev, node:
                if not pair:
                    continue
                descending = False
                if pair.next:
                    heapq.heappush(heap, (pair.value + pair.next.value, pair.i, pair))
                    descending = pair.value > pair.next.value
                num_descending += descending - pair.descending
                pair.descending = descending
        
        return num_operations










if __name__ == "__main__":
    sol = Solution()
    tests = [
        [5,2,3,1],
        [1,2,2],
    ]

    for nums in tests:
        res = sol.minimumPairRemoval(nums)
        print(res)