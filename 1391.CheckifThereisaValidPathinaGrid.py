# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/?envType=daily-question&envId=2026-04-27

from typing import List
from collections import deque


UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


street_connects = {
    1: {LEFT, RIGHT},
    2: {UP, DOWN},
    3: {LEFT, DOWN},
    4: {RIGHT, DOWN},
    5: {UP, LEFT},
    6: {UP, RIGHT},
}


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        R = len(grid)
        C = len(grid[0])

        visited = set()
        queue = deque([(0, 0, -1, -1)])

        def get_reachable_neighbours(x, y):
            result = []
            for direction in street_connects[grid[x][y]]:
                match direction:
                    case 0: # UP
                        if x - 1 >= 0 and (DOWN in street_connects[grid[x - 1][y]]):
                            result.append((x - 1, y))
                    case 1: # RIGHT
                        if y + 1 < C and (LEFT in street_connects[grid[x][y + 1]]):
                            result.append((x, y + 1))
                    case 2: # DOWN
                        if x + 1 < R and (UP in street_connects[grid[x + 1][y]]):
                            result.append((x + 1, y))
                    case 3: # LEFT
                        if y - 1 >= 0 and (RIGHT in street_connects[grid[x][y - 1]]):
                            result.append((x, y - 1))
            return result

        
        while queue:
            x, y, px, py = queue.popleft()

            if x == R - 1 and y == C - 1:
                return True

            visited.add((x, y))

            for neighbour in get_reachable_neighbours(x, y):
                if neighbour in visited or neighbour == (px, py):
                    continue
                
                queue.append((neighbour[0], neighbour[1], x, y))
        
        return False
                


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[2,4,3],[6,5,2]],
        [[1,2,1],[1,2,1]],
        [[1,1,2]],
    ]

    for g in tests:
        res = sol.hasValidPath(g)
        print(res)
