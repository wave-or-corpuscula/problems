# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2026-02-26

class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)

        count = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "1101"
        "10",
        "1"
    ]