# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.lower()))
        left = 0
        right = len(s) - 1

        while right > left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True
    

class ElegantSolution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

        
if __name__ == "__main__":
    sol = Solution()
    tests = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]

    for s in tests:
        res = sol.isPalindrome(s)
        print(res)