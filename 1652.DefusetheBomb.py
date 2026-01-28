# https://leetcode.com/problems/defuse-the-bomb/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)

        result = []

        def next_sum():
            result.append(sum(code[i % N] for i in range(1, k + 1)))
            for i in range(1, N):
                result.append(result[i - 1] - code[i] + code[(i + k) % N])

        def prev_sum():
            result.append(sum(code[i] for i in range(-1, k - 1, -1)))
            for i in range(1, N):
                result.append(result[i - 1] + code[i - 1] - code[i - 1 + k ])
            

        if k > 0:
            next_sum()
        elif k == 0:
            return [0] * N
        else:
            prev_sum()

        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,4,9,3], 2),
        ([5,7,1,4], 2),
        ([2,4,9,3], -2),
        ([1,2,3,4], 0),
    ]
    for nums, k in tests:
        res = sol.decrypt(nums, k)
        print(res)