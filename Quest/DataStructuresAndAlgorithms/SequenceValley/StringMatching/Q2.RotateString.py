# https://leetcode.com/problems/rotate-string/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) == len(s) and goal in (s + s)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcde", "cdeab"),
        ("abcde", "abced"),
    ]

    for s, goal in tests:
        res = sol.rotateString(s, goal)
        print(res)