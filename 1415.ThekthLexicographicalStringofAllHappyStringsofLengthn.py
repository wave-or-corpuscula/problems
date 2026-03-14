# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2026-03-14

from itertools import product


class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def happy(s: tuple) -> bool:
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        all_strs = list(product("abc", repeat=n))
        happy_strs = list(filter(happy, all_strs))

        if len(happy_strs) < k:
            return ""
        
        return "".join(happy_strs[k - 1])


class FastestSolution:
    def getHappyString(self, n: int, k: int) -> str:
        # Для n=1: 3 строки
        # Для каждой следующей позиции: умножаем на 2 (нельзя повторять предыдущую)
        total = 3 * (2 ** (n - 1)) if n > 0 else 0
        
        if total < k:
            return ""
        
        result = []
        prev = ''
        
        for i in range(n):
            # Перебираем буквы в лексикографическом порядке
            for c in 'abc':
                if c == prev:
                    continue
                
                # Сколько строк будет, если выберем эту букву?
                remaining = n - i - 1
                if remaining == 0:
                    count = 1
                else:
                    count = 2 ** remaining  # На каждую позицию по 2 варианта
                
                if k <= count:
                    result.append(c)
                    prev = c
                    break
                else:
                    k -= count
        
        return ''.join(result)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, 3),
        (1, 4),
        (3, 9),
    ]

    for n, k in tests:
        res = sol.getHappyString(n, k)
        print(res)
