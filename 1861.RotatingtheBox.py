# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2026-05-06

from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        R = len(boxGrid)
        C = len(boxGrid[0])
        
        rotated_grid = [['.'] * R for _ in range(C)]

        for i in range(R - 1, -1, -1):
            bottom = C - 1
            for j in range(C - 1, -1, -1):
                if boxGrid[i][j] == "#":
                    rotated_grid[bottom][R - i - 1] = "#"
                    bottom -= 1
                elif boxGrid[i][j] == "*":
                    rotated_grid[j][R - i - 1] = "*"
                    bottom = j - 1
        
        return rotated_grid

    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [["#",".","#"]],

        [["#",".","*","."],
         ["#","#","*","."]],

        [["#","#","*",".","*","."],
         ["#","#","#","*",".","."],
         ["#","#","#",".","#","."]],
    ]

    for grid in tests:
        res = sol.rotateTheBox(grid)
        print(res)