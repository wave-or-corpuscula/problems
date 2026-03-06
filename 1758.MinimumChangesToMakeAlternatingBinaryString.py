# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05

class Solution:
    def minOperations(self, s: str) -> int:
        """
        
        0100
          ^

        010010101010000
           101010101

        0000000
         1 1 1
        """
        N = len(s)
        start1 = 0
        start0 = 0

        for i in range(N):
            if i % 2 == 0:
                if s[i] == '1':
                    start0 += 1
                else:
                    start1 += 1
            else:
                if s[i] == '0':
                    start0 += 1
                else:
                    start1 += 1
        return min(start0, start1)






if __name__ == "__main__":
    sol = Solution()
    tests = [
        "110010",
        "0010100",
        "0100",
        "01010",
        "1111",
    ]

    for s in tests:
        res = sol.minOperations(s)
        print(res)