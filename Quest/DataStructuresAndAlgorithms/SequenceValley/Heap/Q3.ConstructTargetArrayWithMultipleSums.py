# https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/?envType=problem-list-v2&envId=dsa-sequence-valley-heap

import heapq

from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]
        total = sum(target)
        # Используем max-heap через отрицательные значения
        heap = [-x for x in target]
        heapq.heapify(heap)
        
        while True:
            max_val = -heapq.heappop(heap)
            if max_val == 1:
                # Все элементы стали 1 (куча пустеет, но мы проверили максимум)
                return True
            sum_rest = total - max_val
            if sum_rest == 1:
                # Особый случай: остальные единицы, этот станет 1 на следующем шаге
                return True
            if max_val <= sum_rest:
                return False
            # Оптимизация: делаем несколько шагов за раз
            steps = (max_val - 1) // sum_rest
            prev = max_val - steps * sum_rest
            if prev < 1:
                return False
            # Обновляем total и возвращаем в кучу
            total = total - max_val + prev
            heapq.heappush(heap, -prev)




        


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [2],
        [9,3,5],
        [1,1,1,2],
        [8,5],
    ]

    for target in tests:
        res = sol.isPossible(target)
        print(res)