# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/?envType=problem-list-v2&envId=sliding-window


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        N = len(s)
        res = 0

        for l in range(1, N + 1):
            freq = [s[:l].count('0'), s[:l].count('1')]
            if any(x <= k for x in freq):
                    res += 1

            for i in range(0, N - l):
                freq[int(s[i])] -= 1
                freq[int(s[i + l])] += 1
                
                if any(x <= k for x in freq):
                    res += 1

        return res


class BestSolution:
    # Идея в том, чтобы считать плохие подстроки и отнимать от общего числа найденные
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2 # Общее количество подстрок

        l = 0
        zeros = ones = 0
        bad = 0

        for r in range(n):
            if s[r] == '0':
                zeros += 1
            else:
                ones += 1

            while zeros > k and ones > k:
                bad += n - r      # все подстроки [l..r], [l..r+1] ... [l..n-1]
                if s[l] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                l += 1

        return total - bad


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("10101",   1),
        ("1010101", 2),
        ("11111",   1),
    ]

    for s, k in tests:
        res = sol.countKConstraintSubstrings(s, k)
        print(res)