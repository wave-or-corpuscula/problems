# https://leetcode.com/problems/walking-robot-simulation-ii/description/?envType=daily-question&envId=2026-04-07

from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = ((width - 1) + (height - 1)) * 2
        self.direction = 0
        self.step_in_dir = [
            self._E_step,
            self._N_step,
            self._W_step,
            self._S_step,
        ]

        self.x = 0
        self.y = 0

    def _E_step(self, num):
        dx = self.x + num
        if dx >= self.width:
            overflow = dx % self.width + 1 + (dx // self.width - 1) * self.width
            self.x = self.width - 1
            return overflow
        self.x = dx
    
    def _N_step(self, num):
        dy = self.y + num
        if dy >= self.height:
            overflow = dy % self.height + 1 + (dy // self.height - 1) * self.height
            self.y = self.height - 1
            return overflow
        self.y = dy

    def _W_step(self, num):
        dx = self.x - num
        if dx < 0:
            self.x = 0
            return abs(dx)
        self.x = dx

    def _S_step(self, num):
        dy = self.y - num
        if dy < 0:
            self.y = 0
            return abs(dy)
        self.y = dy
        
    def _turn_left(self):
        self.direction = (self.direction + 1) % 4

    def step(self, num: int) -> None:
        num %= self.perimeter

        if num == 0:
            num = self.perimeter

        if overflow := self.step_in_dir[self.direction](num):
            self._turn_left()
            self.step(overflow)

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.direction]


class BetterRobot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height - 2)
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        
        if p < self.w:
            return [p, 0]
        elif p < self.w + self.h - 1:
            return [self.w - 1, p - (self.w - 1)]
        elif p < 2 * self.w + self.h - 2:
            return [(self.w - 1) - (p - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.perimeter - p]

    def getDir(self) -> str:
        p = self.pos
        
        if p == 0:
            return "South" if self.moved else "East"
            
        if p < self.w:
            return "East"
        elif p < self.w + self.h - 1:
            return "North"
        elif p < 2 * self.w + self.h - 2:
            return "West"
        else:
            return "South"


if __name__ == "__main__":
    rob = Robot(3, 2)
    # rob.step(2)
    # rob.step(2)
    # print(rob.getPos())
    # print(rob.getDir())
    # rob.step(2)
    # print(rob.getPos())
    # rob.step(1)
    # rob.step(4)
    # print(rob.getPos())
    # print(rob.getDir())
    rob.step(6)
    print(rob.getPos())
    print(rob.getDir())

    

    