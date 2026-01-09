# https://leetcode.com/problems/climbing-stairs/

n = 46
s = [1]* n

s[0] = 1
s[1] = 2

for i in range(2, n):
    s[i] = s[i - 1] + s[i - 2]


class MyFastestRuntimeSolution:
    def climbStairs(self, n: int) -> int:
        return s[n - 1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        one_stair = 1
        two_stairs = 2
        for _ in range(2, n):
            steps = two_stairs + one_stair
            one_stair = two_stairs
            two_stairs = steps
        return steps

if __name__ == "__main__":
    sol = MyFastestRuntimeSolution()
    tests = [
        2, 3, 4, 5
    ]
    for test in tests:
        print(sol.climbStairs(test))