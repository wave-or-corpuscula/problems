# https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2026-04-01

from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        x = x0 + v * t
        10
        RL  RL
        123456789
        """
        N = len(positions)

        going_left = {}
        going_right = {}

        collisions = []

        for i in range(N):
            if directions[i] == "R":
                going_right[positions[i]] = (i + 1, healths[i])
            else:
                going_left[positions[i]] = (i + 1, healths[i])

        while going_right and going_left:
            
            if min(going_right.keys()) > max(going_left.keys()):
                break

            print(going_right)
            print(going_left)

            # Проблема два раза добавляется один индекс из going_left
            for pos in going_right.keys():
                if (pos in going_left):
                    collisions.append((pos, pos))
                elif (pos + 1 in going_left):
                    collisions.append((pos, pos + 1))
            
            
            while collisions:
                rpos, lpos = collisions.pop()
                rnum, right_health = going_right.pop(rpos)
                lnum, left_health = going_left.pop(lpos)

                if right_health > left_health:
                    going_right[rpos] = (rnum, right_health - 1)
                elif left_health > right_health:
                    going_left[lpos] = (lnum, left_health - 1)

            going_right = {k + 1: v for k, v in going_right.items()}
            going_left = {k - 1: v for k, v in going_left.items()}

        result = list(going_left.values())
        result.extend(going_right.values())
        result.sort()

        return [h for _, h in result]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,5,2,6],   [10,10,15,12],  "RLRL"),
        # ([6,5], [100, 100], "RL"),
        # ([1,2,5,7, 100],   [10,10,11,12, 100],  "RLRLL"),
        # ([5,4,3,2,1], [2,17,9,15,10], "RRRRR"),
    ]
    
    for pos, h, direc in tests:
        res = sol.survivedRobotsHealths(pos, h, direc)
        print(res)