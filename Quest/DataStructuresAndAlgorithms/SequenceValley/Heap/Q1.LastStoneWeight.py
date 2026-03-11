# https://leetcode.com/problems/last-stone-weight/description/?envType=problem-list-v2&envId=dsa-sequence-valley-heap

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        priority_stones = [(-x, x) for x in stones]
        heapq.heapify(priority_stones)
        while len(priority_stones) > 1:
            _, w1 = heapq.heappop(priority_stones)
            _, w2 = heapq.heappop(priority_stones)

            new_stone = w1 - w2
            if new_stone == 0:
                continue

            heapq.heappush(priority_stones, (-new_stone, new_stone))
        
        if priority_stones:
            _, w = heapq.heappop(priority_stones)
            return w
        
        return 0


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [2,7,4,1,8,1],
        [2,7,4,100,8,1],
        [1],
    ]

    for stones in tests:
        res = sol.lastStoneWeight(stones)
        print(res)