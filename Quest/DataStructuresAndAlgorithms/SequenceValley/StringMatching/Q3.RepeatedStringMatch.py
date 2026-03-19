# https://leetcode.com/problems/repeated-string-match/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        A = len(a)
        B = len(b)

        if B == 0:
            return 0

        if b in a:
            return 1
        
        if A > B:
            if b in a * 2:
                return 2
            return -1

        count = A // B

        if set(a) != set(b):
            return -1

        while B >= A * (count - 2):
            
            if b in a * count:
                return count

            count += 1
        return -1


class BetterSolution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = (len(b) - 1) // len(a) + 1
        
        # Проверяем это количество и на одно больше
        for i in range(repeat, repeat + 2):
            if b in a * i:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abc", "cabcabca"),
        ("aa",    "a"),
        ("a",    "aa"),
        ("abcd", "cdabcdab"),
    ]

    for a, b in tests:
        res = sol.repeatedStringMatch(a, b)
        print(res)