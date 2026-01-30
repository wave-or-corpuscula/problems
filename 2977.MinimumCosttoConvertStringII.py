# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/?envType=daily-question&envId=2026-01-30

from typing import List

from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = 10 ** 20

        transformation_graph = defaultdict(dict)
        cached_costs = {}
        for src_sub, tgt_sub, transform_cost in zip(original, changed, cost):
            transformation_graph[src_sub][tgt_sub] = min(
                transform_cost,
                transformation_graph[src_sub].get(tgt_sub, inf)
            )
        def get_min_cost(start_substring: str, end_substring: str) -> int:
            if start_substring in cached_costs:
                return cached_costs[start_substring].get(end_substring, inf)
            min_heap = [(0, start_substring)]
            min_distance = {start_substring: 0}
            while min_heap:
                current_cost, current_sub = heappop(min_heap)
                if current_cost != min_distance[current_sub]:
                    continue
                for next_sub, edge_cost in transformation_graph[current_sub].items():
                    new_cost = current_cost + edge_cost
                    if new_cost < min_distance.get(next_sub, inf):
                        min_distance[next_sub] = new_cost
                        heappush(min_heap, (new_cost, next_sub))
            cached_costs[start_substring] = min_distance
            return min_distance.get(end_substring, inf)
        string_length = len(source)
        possible_lengths = sorted(set(len(sub) for sub in original))
        dp = [inf] * (string_length + 1)
        dp[0] = 0
        for start_index in range(string_length):
            if dp[start_index] == inf:
                continue

            # Case 1: characters already match
            if source[start_index] == target[start_index]:
                dp[start_index + 1] = min(dp[start_index + 1], dp[start_index])

            # Case 2: try substring transformations
            for length in possible_lengths:
                end_index = start_index + length
                if end_index > string_length:
                    break

                source_sub = source[start_index:end_index]
                target_sub = target[start_index:end_index]

                if source_sub in transformation_graph:
                    transform_cost = get_min_cost(source_sub, target_sub)
                    dp[end_index] = min(dp[end_index], dp[start_index] + transform_cost)

        return -1 if dp[string_length] == inf else dp[string_length]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]),
        ("abcdefgh", "acdeeghh", ["bcd","fgh","thh"], ["cde","thh","ghh"], [1,3,5]),
        ("abcdefgh", "addddddd", ["bcd","defgh"], ["ddd","ddddd"], [100,1578]),
    ]

    for s, t, o, ch, co in tests:
        res = sol.minimumCost(s, t, o, ch, co)
        print(res)