# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/?envType=daily-question&envId=2026-03-01

class Solution:
    def minPartitions(self, n: str) -> int:
        ord_base = 48
        max_ord = 57
        max_dig = ord_base
        for x in n:
            max_dig = max(max_dig, ord(x))
            if max_dig == max_ord:
                return 9
        return max_dig - ord_base
        


class BestSolution:
    def minPartitions(self, n: str) -> int:
        for d in "987654321":
            if d in n:
                return int(d)     
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "32", 
        "82734", 
        "27346209830709182346"
    ]

    for n in tests:
        res = sol.minPartitions(n)
        print(res)