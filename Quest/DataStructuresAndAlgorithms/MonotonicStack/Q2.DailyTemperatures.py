# https://leetcode.com/problems/daily-temperatures/description/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack

from typing import List


class Solution:
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
