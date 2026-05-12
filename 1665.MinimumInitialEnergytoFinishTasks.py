# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/?envType=daily-question&envId=2026-05-12

from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: (task[1] - task[0]), reverse=True)
        
        def calc(energy):
            spent = 0
            for actual, minimum in tasks:
                if (energy - spent) < minimum:
                    break
                spent += actual
            else:
                return True
            return False
        
        min_energy = sum(t[0] for t in tasks)
        max_energy = sum(t[1] for t in tasks)

        if min_energy == max_energy:
            return min_energy

        best = float("inf")
        while min_energy < max_energy:
            mid = (min_energy + max_energy) // 2
            
            if calc(mid):
                best = min(best, mid)
                max_energy = mid
            else:
                min_energy = mid + 1
        return best


class BetterSolution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1] - t[0])
        need = 0
        for actual, minimum in tasks:
            need = max(minimum, need + actual)
        return need


if __name__ == "__main__":
    sol = BetterSolution()
    
    tests = [
        [[1,2],[2,4],[4,8]],
        [[1,3],[2,4],[10,11],[10,12],[8,9]],
        [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]],
    ]

    for tasks in tests:
        res = sol.minimumEffort(tasks)
        print(res)