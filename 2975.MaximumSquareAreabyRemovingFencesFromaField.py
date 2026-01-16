# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/?envType=daily-question&envId=2026-01-16

from typing import List, Set


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def all_contiguous_sums(segments):
            sums = set()
            for i in range(len(segments)):
                s = 0
                for j in range(i, len(segments)):
                    s += segments[j]
                    sums.add(s)
            return sums
        
        hfences = sorted([1] + hFences + [m])
        vfences = sorted([1] + vFences + [n])

        h_segments = [hfences[i+1] - hfences[i] for i in range(len(hfences)-1)]
        v_segments = [vfences[i+1] - vfences[i] for i in range(len(vfences)-1)]

        if len(h_segments) < len(v_segments):
            small, big = h_segments, v_segments
        else:
            small, big = v_segments, h_segments

        small_sums = all_contiguous_sums(small)

        best = 0
        for i in range(len(big)):
            s = 0
            for j in range(i, len(big)):
                s += big[j]
                if s > max(small_sums):
                    break
                if s in small_sums:
                    best = max(best, s)
        if best:
            return best * best % (10 ** 9 + 7)
        return -1
        



if __name__ == "__main__":
    sol = Solution()
    tests = [
        (4, 3, [2,3], [2]),
        (6, 7, [2], [4]),
    ]

    for m, n, hfences, vfences in tests:
        res = sol.maximizeSquareArea(m, n, hfences, vfences)
        print(res)