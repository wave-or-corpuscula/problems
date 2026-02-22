# https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        size = len(bin(n)) - 3

        current = 1
        
        while size + 1:
            if current ^ ((n >> size) & 1):
                return False
            size -= 1
            current = 0 if current else 1
        return True
    
class BetterSolution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Если биты чередуются, то n ^ (n >> 1) даст все единицы
        temp = n ^ (n >> 1)
        # Проверяем, что temp - это число вида 111...111
        return (temp & (temp + 1)) == 0


class BitsIterationSolution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n >>= 1

        while n:
            current = n & 1
            if current == prev:
                return False
            prev = current
            n >>= 1
        return True



if __name__ == "__main__":
    sol = BitsIterationSolution()

    tests = [
        5, 7, 11
    ]

    for n in tests:
        res = sol.hasAlternatingBits(n)
        print(res)