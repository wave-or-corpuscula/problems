# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/?envType=daily-question&envId=2026-03-22

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        
        [0,0,0],    [1,1,1],  1 0 0
        [0,1,0],    [0,1,0],  1 1 0
        [1,1,1]     [0,0,0]   1 0 0
        
        """

        # N = len(mat)
        # ROTS = [90, 180, 270]
        # target_transp = [list(row) for row in zip(*target)][::-1]

        # def row_in_target(i, row, rot) -> bool:
        #     match rot:
        #         case 90:
        #             return row == target_transp[i]
        #         case 180:
        #             return row == target[-(i + 1)]
        #         case 270:
        #             return row == target_transp[-(i + 1)]

                
        # for rot in ROTS:
        #     for i, row in enumerate(mat):
        #         if not row_in_target(i, row, rot):
        #             break
        #     else:
        #         return True
        # return False

        if mat == target:
            return True

        def rotate_90(matrix):
            return [list(row)[::-1] for row in zip(*matrix)]

        rot_90 = rotate_90(mat)
        if target == rot_90:
            return True
        
        rot_180 = rotate_90(rot_90)
        if target == rot_180:
            return True
        
        rot_270 = rotate_90(rot_180)
        if target == rot_270:
            return True
        
        return False


class SolutionButBetter:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): 
            if mat == target: 
                return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False 


if __name__ == "__main__":
    sol = Solution()
    tests = [
        # ([[1,1],[0,1]], [[1,1],[1,0]]),
        # ([[0,0],[0,1]], [[0,0],[1,0]]),
        # ([[0,1],[1,0]],             [[1,0],[0,1]]),
        # ([[0,1],[1,1]],             [[1,0],[0,1]]),
        ([[1,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,1]]),
    ]

    for mat, tar in tests:
        res = sol.findRotation(mat, tar)
        print(res)
