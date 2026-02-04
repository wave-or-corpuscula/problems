# https://leetcode.com/problems/trionic-array-ii/description/?envType=daily-question&envId=2026-02-04

from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        N = len(nums)
        
        i = 0
        increase = True
        tritonic = [increase, not increase, increase]
        result = [-1]
        peak_indxs = []
        while i < N - 1:
            if nums[i + 1] > nums[i] and result[-1] is not increase:
                result.append(increase)
                peak_indxs.append(i)
            elif nums[i + 1] < nums[i] and result[-1] is not (not increase):
                result.append(not increase)
                peak_indxs.append(i)
            elif nums[i + 1] == nums[i]:
                result.append(-1)
                peak_indxs.append(i)
            i += 1
        if peak_indxs[-1] != N - 1:
            peak_indxs.append(N - 1)
        result.pop(0)

        # print(nums)
        # print(result)
        # print(peak_indxs)

        INF = 10 ** 20
        best = -INF
        # print(peak_indxs)
        # print(nums)
        pref = [0]
        for x in nums:
            pref.append(pref[-1] + x)

        def get_sum(l, r):
            return pref[r] - pref[l]

        best = -10**20
        for i in range(len(result) - 2):
            if result[i:i + 3] == tritonic:
                l = peak_indxs[i]
                r = peak_indxs[i + 3] + 1
                best = max(best, get_sum(l, r))

                # for x in range(peak_indxs[i], peak_indxs[i + 1]):
                #     for y in range(peak_indxs[i + 2] + 2, peak_indxs[i + 3] + 2):
                #         print(f"nums[{x}:{y}] = {nums[x:y]}")
                #         best = max(best, sum(nums[x:y]))

                #     # best = max(best, sum(nums[peak_indxs[i]:peak_indxs[i + 3] + 1]))
                # print(f"{result[i:i + 3]}, {peak_indxs[i], peak_indxs[i + 3] + 1}")

        # for i in range(N):
        #     print(nums[i], end="  ")
        #     if peak_indxs and i == peak_indxs[0]:
        #         print(peak_indxs.pop(0), result.pop(0))
        #     else:
        #         print()


        return best
    
class NotMySolution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        i = 0

        while i < n:
            j = i + 1
            res = 0

            # first segment: increasing segment
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1

            if p == i:  # 没有有效的increasing segment
                i += 1
                continue

            # second segment: decreasing segment
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1

            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue

            # third segment: increasing segment
            res += nums[q + 1]

            # find the maximum sum of the third segment
            max_sum = 0
            curr_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
                k += 1
            res += max_sum

            # find the maximum sum of the first segment
            max_sum = 0
            curr_sum = 0
            for k in range(p - 2, i - 1, -1):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
            res += max_sum

            # update answer
            ans = max(ans, res)
            i = q

        return ans


if __name__ == "__main__":
    sol = NotMySolution()
    tests = [
        [2,993,-791,-635,-569],
        [1,4,2,7],
        [0,-2,-1, 0, 1, -3, -4, 0, 2,-1],
        [0,-2,-1,-3,0,2,-1],
    ]

    for nums in tests:
        res = sol.maxSumTrionic(nums)
        print(res)