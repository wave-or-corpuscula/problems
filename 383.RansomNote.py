# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        ### My Variation
        # ransom_d = Counter(ransomNote)
        # magazine_d = Counter(magazine)

        # for letter, freq in ransom_d.items():
        #     if magazine_d[letter] < freq:
        #         return False
        # return True

        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True