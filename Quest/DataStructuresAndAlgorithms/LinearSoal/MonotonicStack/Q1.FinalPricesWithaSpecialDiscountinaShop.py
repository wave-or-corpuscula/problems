# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        final = []

        for i in range(N):
            price = prices[i]
            for j in range(i + 1, N):
                if prices[j] <= price:
                    price -= prices[j]
                    break
            final.append(price)
        return final
    

if __name__ == "__main__":
    pass
            

