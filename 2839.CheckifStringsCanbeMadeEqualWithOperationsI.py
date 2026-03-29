# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/?envType=daily-question&envId=2026-03-29


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """
        
        abcdefghijkl
         ^
        ajcdefghibkl
                 ^
        
        """
        N = len(s1)

        s1 = list(s1)
        s2 = list(s2)

        for i in range(N):
            if s1[i] == s2[i]:
                continue

            for j in range(i, N, 2):
                if s1[i] == s2[j]:
                    s2[i], s2[j] = s2[j], s2[i]
                    break
            else:
                return False
        
        return True


class ConstSolution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        
        
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])

        return even_s1 == even_s2 and odd_s1 == odd_s2