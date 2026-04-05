# https://leetcode.com/problems/decode-the-slanted-ciphertext/description/?envType=daily-question&envId=2026-04-04


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1 or not encodedText:
            return encodedText
        
        colls = len(encodedText) // rows
        enc_table = [[' '] * colls for _ in range(rows)]
        for i in range(len(encodedText)):
            enc_table[i // colls][i % colls] = encodedText[i]
        
        decoded = []

        for j in range(colls):
            diagonal = []
            for i in range(rows):
                col = i + j
                if col < colls:
                    diagonal.append(enc_table[i][col])
            if diagonal:
                decoded.extend(diagonal)
                    
        
        return "".join(decoded).rstrip()



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("a  b  ", 3),
        # ("iveo    eed   l te   olc",  4),
        # ("a ", 2),
        # ("ch   ie   pr", 3),
        # ("coding",       1),
    ]

    for e, r in tests:
        res = sol.decodeCiphertext(e, r)
        print(res)