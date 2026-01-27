# 

import heapq

from typing import List

from collections import defaultdict

# Изучить алгоритм Дийкстрыд

class Solution:
    def minCost(self, N: int, edges: List[List[int]]) -> int:
        INF = 10 ** 20

        e = defaultdict(list)

        for u, v, w in edges:
            e[u].append((v, w))
            e[v].append((u, w * 2))

        best = [INF] * N
        best[0] = 0

        h = []
        heapq.heappush(h, (0, 0))

        while h:
            d, node = heapq.heappop(h)

            if node == N - 1:
                return best[node]
            
            if best[node] != d:
                continue

            for v, w in e[node]:
                if best[node] + w < best[v]:
                    best[v] = best[node] + w
                    heapq.heappush(h, (best[v], v))
        return -1
