# https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/valid-mountain-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-assignment-i

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        if N < 3 or arr[0] > arr[1]:
            return False

        found_peak = False

        for i in range(N - 1):
            if arr[i + 1] == arr[i]:
                return False
            
            if found_peak:
                if arr[i + 1] > arr[i]:
                    return False
            else:
                if arr[i + 1] < arr[i]:
                    found_peak = True
                    continue
                if arr[i + 1] < arr[i]:
                    return False
        
        print(f"Found peak: {found_peak}")
        return found_peak

print("result:", Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9]))
print("result:", Solution().validMountainArray([0,1,2,4,2,1]))
print("result:", Solution().validMountainArray([2,1]))
print("result:", Solution().validMountainArray([3,5,5]))
print("result:", Solution().validMountainArray([0,3,2,1]))