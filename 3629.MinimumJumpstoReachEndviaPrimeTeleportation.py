# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/?envType=daily-question&envId=2026-05-08

from collections import defaultdict, deque
from math import inf
from typing import List


MAX = 10 ** 6 + 5
primes = [x for x in range(MAX)]
primes[0] = primes[1] = -1

for i in range(2, MAX):
    if primes[i] == i:
        j = i * i
        while j < MAX:
            primes[j] = i
            j += i


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        N = len(nums)

        f = defaultdict(set)

        for i in range(N):
            if nums[i] in [0, 1]:
                continue

            current = nums[i]
            while primes[current] != current:
                f[primes[current]].add(i)
                current //= primes[current]
            f[primes[current]].add(i)

        fd = set()

        best = [inf] * N
        best[0] = 0

        q = deque()
        q.append(0)

        while q:
            now = q.popleft()

            for dx in [-1, 1]:
                if 0 <= now + dx < N and best[now + dx] == inf:
                    best[now + dx] = best[now] + 1
                    q.append(now + dx)
            
            if primes[nums[now]] == nums[now] and nums[now] not in fd:
                fd.add(nums[now])

                for x in f[nums[now]]:
                    if best[x] == inf:
                        best[x] = best[now] + 1
                        q.append(x)
        return best[N - 1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,2,4,6],
        [2,3,4,7,9],
        [4,6,5,8],
    ]

    for nums in tests:
        res = sol.minJumps(nums)
        print(res)
            
