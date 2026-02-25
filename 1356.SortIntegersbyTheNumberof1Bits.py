# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2026-02-25

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sort_key(x: int) -> tuple[int, int]:
            ones_cnt = bin(x).count('1')
            return (ones_cnt, x)
        return sorted(arr, key=sort_key)

    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [0,1,2,3,4,5,6,7,8],
        [1024,512,256,128,64,32,16,8,4,2,1]
    ]

    for arr in tests:
        res = sol.sortByBits(arr)
        print(res)
    



