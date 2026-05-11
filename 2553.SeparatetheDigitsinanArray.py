# https://leetcode.com/problems/separate-the-digits-in-an-array/description/?envType=daily-question&envId=2026-05-11

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        """
        
        [13, 25]

        digits = 5,2

        
        """

        result = [int(s) for num in nums for s in str(num)]
        # for num in nums:
        #     for s in str(num):
        #         result.append(int(s))
        
        return result
            

class ClenerSolution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num < 10:
                result.append(num)
            else:
                for s in str(num):
                    result.append(int(s))
        return result
