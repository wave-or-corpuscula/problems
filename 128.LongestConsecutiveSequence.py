# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))

        unique_nums.sort()
        N = len(unique_nums)
        longest = 0
        cur_length = 1
        for i in range(1, N):
            if unique_nums[i - 1] + 1 == unique_nums[i]:
                cur_length += 1
            else:
                longest = max(longest, cur_length)
                cur_length = 1
        longest = max(longest, cur_length)
        return longest
    
class CorrectSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for x in num_set:
            if x-1 not in num_set:
                current=x
                count=1

                while current+1 in num_set:
                    current+=1
                    count+=1
                longest=max(longest,count)
        return longest
            

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [100,4,200,1,3,2],
    ]
    for test in tests:
        res = sol.longestConsecutive(test)
        print(res)