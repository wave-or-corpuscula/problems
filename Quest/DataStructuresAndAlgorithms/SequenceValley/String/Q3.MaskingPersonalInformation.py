# https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string


class Solution:
    def maskPII(self, s: str) -> str:
        
        def mask_email(email: str) -> str:
            lower = email.lower()
            name, domain = lower.split('@')
            masked_name = f"{name[0]}*****{name[-1]}"
            return f"{masked_name}@{domain}"
        
        def mask_phone(phone: str) -> str:
            trans_table = str.maketrans('', '', "-+() ")
            clear = phone.translate(trans_table)

            rest_len = len(clear) - 4
            first_char = '+' if rest_len > 6 else ''
            return f"{first_char}{'*' * (rest_len % 6)}{'-' if first_char else ''}***-***-{clear[-4:]}"
        
        if '@' in s:
            return mask_email(s)
        else:
            return mask_phone(s)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "1(234)567-890",
        "LeetCode@LeetCode.com",
        "AB@qq.com",
    ]

    for s in tests:
        res = sol.maskPII(s)
        print(res)