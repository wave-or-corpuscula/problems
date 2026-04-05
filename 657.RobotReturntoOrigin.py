# https://leetcode.com/problems/robot-return-to-origin/description/?envType=daily-question&envId=2026-04-05

from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = Counter(moves)
        return moves.get("U") == moves.get("D") and moves.get("L") == moves.get("R")
    

class AnotherSolution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "UD",
        "LL",
    ]
    for move in tests:
        res = sol.judgeCircle(move)
        print(res)