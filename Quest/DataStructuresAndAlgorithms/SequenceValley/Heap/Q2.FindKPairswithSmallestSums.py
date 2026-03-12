# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=problem-list-v2&envId=dsa-sequence-valley-heap


import heapq
from typing import List
from itertools import product


class BurtalBrutalForceSolution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        all_pairs = sorted(product(nums1, nums2), key=sum)
        return all_pairs[:k]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Если один из массивов пуст, возвращаем пустой список
        if not nums1 or not nums2:
            return []
        
        # Min-heap (куча минимумов) будет хранить (сумма, индекс в nums1, индекс в nums2)
        heap = []
        
        # Инициализация: для первых min(len(nums1), k) элементов nums1
        # добавляем пару с nums2[0]
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
            print(heap)
        
        result = []
        
        # Собираем k наименьших пар
        while heap and len(result) < k:
            # Извлекаем пару с наименьшей суммой
            sum_val, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # Если можем двигаться дальше по второму массиву
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,2],  [1,2,3], 4),
        # ([1,7,11], [2,4,10], 6),
    ]

    for n1, n2, k in tests:
        res = sol.kSmallestPairs(n1, n2, k)
        print(res)
