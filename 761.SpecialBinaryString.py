# https://leetcode.com/problems/special-binary-string/description/?envType=daily-question&envId=2026-02-20

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []

        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                middle_optimized = self.makeLargestSpecial(s[i + 1:j])
                res.append(f"1{middle_optimized}0")
                i = j + 1
        
        res.sort(reverse=True)
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "11011000",
        "10"
    ]

    for s in tests:
        res = sol.makeLargestSpecial(s)
        print(res)
