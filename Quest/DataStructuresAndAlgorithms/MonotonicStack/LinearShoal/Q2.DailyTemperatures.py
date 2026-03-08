# https://leetcode.com/problems/daily-temperatures/description/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack

from typing import List


class SlowSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        answer = []

        for i in range(N):
            days = 0
            found = False
            for j in range(i + 1, N):
                days += 1
                    
                if temperatures[j] > temperatures[i]:
                    found = True
                    break
            if not found:
                days = 0
            answer.append(days)
        return answer


class MonotonicStackSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):

            if not stack or temp <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    ind = stack.pop()
                    ans[ind] = i - ind
                stack.append(i)

        return ans


if __name__ == "__main__":
    sol = MonotonicStackSolution()
    tests = [
        [73,74,75,71,69,72,76,73],
        [30,40,50,60],
        [30,60,90],
    ]

    for t in tests:
        res = sol.dailyTemperatures(t)
        print(res)