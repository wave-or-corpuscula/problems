# https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        N = len(nums)
        triplets = []
        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, N - 1

            while left < right:
                s = nums[left] + nums[right]
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return triplets


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
    ]

    for n in tests:
        res = sol.threeSum(n)
        print(res)