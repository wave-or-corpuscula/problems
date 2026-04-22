# https://leetcode.com/problems/words-within-two-edits-of-dictionary/?envType=daily-question&envId=2026-04-22

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        REPLACES = 2

        result = []
        for query in queries:
            for word in dictionary:
                replaced = 0
                for q, w in zip(query, word):
                    if q != w:
                        replaced += 1
                    if replaced > REPLACES:
                        break
                else:
                    result.append(query)
                    break

        return result



if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["word","note","ants","wood"], ["wood","joke","moat"]),
        (["yes"], ["not"]),
    ]

    for q, d in tests:
        res = sol.twoEditWords(q, d)
        print(res)