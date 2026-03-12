# https://leetcode.com/problems/license-key-formatting/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        clean = s.replace('-', '').upper()
        
        result = []
        for i in range(len(clean), 0, -k):
            start = max(0, i - k)
            result.append(clean[start:i])

        return '-'.join(reversed(result))



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("5F3Z-2e-9-w", 4),
        ("2-5g-3-J",    2),
    ]
    for s, k in tests:
        res = sol.licenseKeyFormatting(s, k)
        print(res)