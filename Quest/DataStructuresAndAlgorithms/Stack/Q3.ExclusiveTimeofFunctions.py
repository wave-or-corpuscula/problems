# https://leetcode.com/problems/exclusive-time-of-functions/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            pid, mode, time = log.split(":")
            pid = int(pid)
            time = int(time)
            
            if mode == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(pid)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return res



if __name__ == "__main__":
    sol = Solution()
    tests = [
        (2, ["0:start:0","1:start:2","1:end:5","0:end:6"]),
        (1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]),
        (2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]),
    ]

    for n, logs in tests:
        res = sol.exclusiveTime(n, logs)
        print(res)