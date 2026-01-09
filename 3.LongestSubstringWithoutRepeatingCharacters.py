# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        start_i = 0
        max_length = 0
        slice = ""
        for end_i in range(1, len(s) + 1):
            while s[end_i - 1] in slice:
                start_i += 1
                slice = s[start_i:end_i - 1]
            else:
                slice = s[start_i:end_i]
            if len(slice) > max_length:
                max_length = len(slice)
        return max_length
    

class SolutionSetVersion:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        max_length = 0
        n = len(s)
        L=0
        for R in range(n):
            while s[R] in seen_set:
                seen_set.remove(s[L])
                L+=1
            w = (R-L)+1
            max_length = max(max_length,w)
            seen_set.add(s[R])
        return max_length
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "au",
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        " ",
    ]

    for test in tests:
        print(sol.lengthOfLongestSubstring(test))