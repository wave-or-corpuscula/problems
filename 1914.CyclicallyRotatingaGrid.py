# https://leetcode.com/problems/cyclically-rotating-a-grid/description/?envType=daily-question&envId=2026-05-09

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        
        [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

         [[1,1,1,1],
         [1,2,2,1],
         [1,2,2,1],
         [1,2,2,1],
         [1,2,2,1],
         [1,1,1,1]]
        
        """
        R = len(grid)
        C = len(grid[0])
        LAYERS = min(R // 2, C // 2)

        for layer in range(LAYERS):
            layer_r = R - layer * 2
            layer_c = C - layer * 2
            layer_n = layer_r * 2 + layer_c * 2 - 4
            layer_elements = [-1] * layer_n
            index = 0
            for i in range(layer_c):
                layer_elements[index] = grid[layer][i + layer]
                index += 1
            for j in range(layer_r - 2):
                layer_elements[index] = grid[layer + j + 1][-(layer + 1)]
                index += 1
            for i in range(layer_c):
                layer_elements[index] = grid[-(layer + 1)][-(i + 1 + layer)]
                index += 1
            for j in range(layer_r - 2):
                layer_elements[index] = grid[-(j + layer + 2)][layer]
                index += 1
            
            K = k % layer_n
            layer_elements = layer_elements[K:] + layer_elements[:K]

            index = 0
            for i in range(layer_c):
                grid[layer][i + layer] = layer_elements[index]
                index += 1
            for j in range(layer_r - 2):
                grid[layer + j + 1][-(layer + 1)] = layer_elements[index]
                index += 1
            for i in range(layer_c):
                grid[-(layer + 1)][-(i + 1 + layer)] = layer_elements[index]
                index += 1
            for j in range(layer_r - 2):
                grid[-(j + layer + 2)][layer] = layer_elements[index]
                index += 1

        return grid
            

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,  2, 3, 4],
          [16, 1, 2, 5],
          [15, 8, 3, 6],
          [14, 7, 4, 7],
          [13, 6, 5, 8],
          [12, 11,10,9]], 2),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2),
        ([[40,10],[30,20]], 1),
    ]

    for grid, k in tests:
        res = sol.rotateGrid(grid, k)
        for row in res:
            print(row)
        print()