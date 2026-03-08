# https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/plus-one/?envType=problem-list-v2&envId=dsa-linear-shoal-assignment-i

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        
        [1,2,3]

        """
        N = len(digits)

        overflow = 1
        for i in range(N - 1, -1, -1):
            res = digits[i] + overflow
            overflow = res // 10
            digits[i] = res % 10

            if overflow == 0:
                break
        return ([1] if overflow else []) + digits
    

print(Solution().plusOne([5, 9, 9]))
print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([4,3,2,1]))
        