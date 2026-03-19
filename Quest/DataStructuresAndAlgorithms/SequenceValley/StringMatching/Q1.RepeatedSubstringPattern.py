# https://leetcode.com/problems/repeated-substring-pattern/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        abab

        substr: all letters, <= str / 2, 

        len(s) == N
        len(subs) == n

        s.count(subs) * n == N

        
        """ 

        N = len(s)

        for i in range(N // 2):
            subs = s[:i + 1]
            n = len(subs)

            if s.count(subs) * n == N:
                return True
        
        return False
    

class SmarterSolution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "abab",
        "aba",
        "abcabcabcabc",
        "c",
    ]

    for s in tests:
        res = sol.repeatedSubstringPattern(s)
        print(res)