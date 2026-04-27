# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/?envType=daily-question&envId=2026-04-26

from typing import List
from collections import deque, defaultdict


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        
        ["a","a","a","a"],
        ["a","b","b","a"],
        ["a","b","b","a"],
        ["a","a","a","a"]
        
        """
        
        R = len(grid)
        C = len(grid[0])
        CELLS = R * C

        if CELLS < 4:
            return False

        visited = defaultdict(set)


        def get_same_neighbours(x, y, fx, fy):
            candidats = [(dx, dy) for dx, dy in 
                         ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                         if (dx, dy) != (fx, fy)]
            return [(dx, dy) for dx, dy in candidats
                    if (0 <= dx < R) and 
                       (0 <= dy < C) and 
                       grid[dx][dy] == grid[x][y]]
        
        def bfs(i, j):
            queue = deque([(i, j, -1, -1)])

            while queue:
                x, y, from_x, from_y = queue.popleft()

                if (x, y) in visited[grid[x][y]]:
                    return True
                
                visited[grid[x][y]].add((x, y))

                for dx, dy in get_same_neighbours(x, y, from_x, from_y):
                    queue.append((dx, dy, x, y))
            
            return False

        for i in range(R):
            for j in range(C):
                if (i, j) not in visited[grid[i][j]]:
                    if bfs(i, j):
                        return True

        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [["a","a","a","a"],
         ["a","b","b","a"],
         ["a","b","b","a"],
         ["a","a","a","a"]],
        [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]],
        [["a","b","b"],["b","z","b"],["b","b","a"]],
    ]

    for g in tests:
        res = sol.containsCycle(g)
        print(res)