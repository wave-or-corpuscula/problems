# https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2026-04-01

from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        )

        stack = []
        alive = [True] * len(robots)

        for i, (pos, health, direction, idx) in enumerate(robots):

            if direction == 'R':
                stack.append(i)
                continue

            while stack and health > 0:
                j = stack[-1]  # последний R
                _, r_health, _, _ = robots[j]

                if r_health < health:
                    # R умирает
                    alive[j] = False
                    stack.pop()
                    health -= 1

                elif r_health > health:
                    # L умирает
                    alive[i] = False
                    robots[j] = (
                        robots[j][0],
                        r_health - 1,
                        robots[j][2],
                        robots[j][3],
                    )
                    health = 0

                else:
                    # оба умирают
                    alive[j] = False
                    alive[i] = False
                    stack.pop()
                    health = 0

            if health > 0:
                robots[i] = (pos, health, direction, idx)
            else:
                alive[i] = False

        # собираем ответ
        res = []
        for i in range(len(robots)):
            if alive[i]:
                res.append((robots[i][3], robots[i][1]))

        res.sort()  # по исходному индексу
        return [h for _, h in res]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([47,26,31,38,35,36], [21,36,9,36,10,38], "RLRLRR")
        # ([3,5,2,6],   [10,10,15,12],  "RLRL"),
        # ([6,5], [100, 100], "RL"),
        # ([1,2,5,7, 100],   [10,10,11,12, 100],  "RLRLL"),
        # ([5,4,3,2,1], [2,17,9,15,10], "RRRRR"),
    ]
    
    for pos, h, direc in tests:
        res = sol.survivedRobotsHealths(pos, h, direc)
        print(res)