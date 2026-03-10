# https://leetcode.com/problems/time-needed-to-buy-tickets/description/?envType=problem-list-v2&envId=dsa-sequence-valley-queue

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        i = 0
        time = 0
        N = len(tickets)
        while tickets[k] != 0:
            if tickets[i % N] != 0:
                tickets[i % N] -= 1
                time += 1
            i += 1
        return time


