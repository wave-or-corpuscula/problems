# https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04


from typing import List



class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        four_divs_sum = 0
        for num in nums:
            divisors = set()
            high = int(num ** 0.5) + 1
            for div in range(1, high):
                if num % div == 0:
                    divisors.add(div)
                    divisors.add(num // div)
                    if len(divisors) > 4:
                        break
            if len(divisors) == 4:
                four_divs_sum += sum(divisors)
            divisors.clear()
        return four_divs_sum
                
# __import__("atexit").register(lambda: open('display_runtime.txt','w').write('0'))

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [6, 8, 9, 10, 11, 12],
        [21,4,7],
        [21,21],
        [1,2,3,4,5],
        [1,2,3,4,5,6,7,8,9,10],
    ]

    for test in tests:
        print(sol.sumFourDivisors(test))