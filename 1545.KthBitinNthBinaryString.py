# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2026-03-03


class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        """
        Si = Si-1 + "1" + reverse(invert(Si - 1))
        1: 0
        2: 011
        3: 0111001
        4: 011100110110001
        """

        start = "0"

        def next(current: str) -> str:
            invert = ["0" if x == "1" else "1" for x in current]
            invert.reverse()
            return "".join([current, "1", "".join(invert)])
        
        for _ in range(n):
            start = next(start)
        
        return start[k - 1]
        


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, 1),
        (4, 11),
    ]

    for n, k in tests:
        res = sol.findKthBit(n ,k)
        print(res)