# https://leetcode.com/problems/closest-equal-element-queries/description/?envType=daily-question&envId=2026-04-16

from typing import List
from collections import defaultdict


class BrutForceSolution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        N = len(nums)

        def _min_distance_to(start: int) -> int:
            target = nums[start]
            i = 1
            for _ in range(N - 1):
                if nums[(i + start) % N] == target or nums[-(i - start) % N] == target:
                    return i
                i += 1
            return -1

        answer = []
        for query in queries:
            answer.append(_min_distance_to(query))

        return answer


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        
        [1,3,1,4,1,3,2]
         0   2   4     

        [1,3,1,4,2,3,1] N = 7  2 + (7 - 6) = 3
        [0   2       6]        6 + (7 - 2) = 12 % 7 = 5

        """
        N = len(nums)

        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)

        def _index(arr, target):

            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1


        def _min_distance(index):
            target = nums[index]

            indexes = positions[target]
            n = len(indexes) 
            if n == 1:
                return -1
            
            target_ind = _index(indexes, index)
            target_pos = indexes[target_ind]

            candidates = [indexes[(target_ind + 1) % n]]
            if n > 2:
                candidates.append(indexes[target_ind - 1])

            return min(
                min(abs(target_pos - ind), N - abs(target_pos - ind))
                for ind in candidates
            )

        answer = []
        for query in queries:
            answer.append(_min_distance(query))

        return answer


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,3,1,4,1,3,2], [0,3,5]),
        ([1,2,3,4], [0,1,2,3]),
    ]
    for n, q in tests:
        res = sol.solveQueries(n, q)
        print(res)