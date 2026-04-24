# https://leetcode.com/problems/furthest-point-from-origin/description/?envType=daily-question&envId=2026-04-24

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        blank = 0

        for move in moves:
            if move == 'L':
                left += 1
            elif move == 'R':
                right += 1
            else:
                blank += 1
        
        return abs(left - right) + blank