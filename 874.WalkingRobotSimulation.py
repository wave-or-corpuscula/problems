# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2026-04-06

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """

          N
        W   E
          S
        
        """

        orientation = 0
        cur_x = 0
        cur_y = 0
        obstacles = set((x, y) for x, y in obstacles)

        best = 0
        
        def turn(comm):
            nonlocal orientation
            if comm == -1:
                orientation += 90
            else:
                orientation += 270
            orientation %= 360

        for command in commands:
            if command < 0:
                turn(command)
                continue
            match orientation:
                case 0:
                    for i in range(command):
                        cur_y += 1
                        if (cur_x, cur_y) in obstacles:
                            cur_y -= 1
                            break
                case 90:
                    for i in range(command):
                        cur_x += 1
                        if (cur_x, cur_y) in obstacles:
                            cur_x -= 1
                            break
                case 180:
                    for i in range(command):
                        cur_y -= 1
                        if (cur_x, cur_y) in obstacles:
                            cur_y += 1
                            break
                case 270:
                    for i in range(command):
                        cur_x -= 1
                        if (cur_x, cur_y) in obstacles:
                            cur_x += 1
                            break
            best = max(best, cur_x ** 2 + cur_y ** 2)
        return best
            



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4,-1,3],      []),
        ([4,-1,4,-2,4], [[2,4]]),
        ([6,-1,-1,6],   [[0,0]])
    ]

    for com, obs in tests:
        res = sol.robotSim(com, obs)
        print(res)