# https://leetcode.com/problems/rotated-digits/description/?envType=daily-question&envId=2026-05-02




class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_rotated_amount = [0] * (n + 1)
        
        def valid_rotated(x):
            x = str(x)
            rotatable = 0
            for ch in x:
                if ch in {'3', '4', '7'}:
                    return 0
                if ch not in {'0', '1', '8'}:
                    rotatable = 1
            return rotatable
            
        for i in range(2, n + 1):
            valid_rotated_amount[i] = valid_rotated_amount[i - 1] + valid_rotated(i)
        
        return valid_rotated_amount[-1]


N = 10 ** 4
valid_rotated_amount = [0] * (N + 1)
        
def valid_rotated(x):
    x = str(x)
    rotatable = 0
    for ch in x:
        if ch in {'3', '4', '7'}:
            return 0
        if ch not in {'0', '1', '8'}:
            rotatable = 1
    return rotatable
    
for i in range(2, N + 1):
    valid_rotated_amount[i] = valid_rotated_amount[i - 1] + valid_rotated(i)


class FasterSolution:
    def rotatedDigits(self, n: int) -> int:
        return valid_rotated_amount[n]



if __name__ == "__main__":
    sol = FasterSolution()
    tests = [
        10, 1, 2
    ]

    for n in tests:
        res = sol.rotatedDigits(n)
        print(res)