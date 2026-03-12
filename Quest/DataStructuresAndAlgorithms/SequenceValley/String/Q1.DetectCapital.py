# https://leetcode.com/problems/detect-capital/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        all_lower = word[0].islower()
        first_cup = not word[0].islower()
        all_cap = first_cup and not word[1].islower()

        if all_lower:
            return all(str.islower(c) for c in word)
        elif all_cap:
            return all(not str.islower(c) for c in word)
        else:
            return all(str.islower(c) for c in word[1:])
        

class FunnySolution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "USA",
        "FlaG",
        "osijosfsf",
    ]
    for test in tests:
        res = sol.detectCapitalUse(test)
        print(res)