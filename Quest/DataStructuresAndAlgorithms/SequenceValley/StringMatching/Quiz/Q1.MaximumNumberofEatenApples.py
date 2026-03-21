# https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/maximum-number-of-eaten-apples/?envType=problem-list-v2&envId=dsa-sequence-valley-assignment-i

from collections import defaultdict
from typing import List

"""

There is a special kind of apple tree that grows apples every day for n days. 
On the ith day, the tree grows apples[i] apples that will rot after days[i] days, 
that is on day i + days[i] the apples will be rotten and cannot be eaten. 
On some days, the apple tree does not grow any apples, 
which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). 
Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

"""


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        apples        days
        [1,2,3,5,2]   [3,2,1,4,2]   


        1 2 3 5 2
        3 2 1 4 2

         1         2           3          4        5             6 7 8 9
        1(3)  2(2) + 1(2)  3(1) + 3(1)  5(4)  2(2) + 5(3)
        
        """

        rotten_in = defaultdict(int)
        eaten = 0
        day = 0
        while apples:
            rotten_in[days.pop(0) + day] += apples.pop()
            day += 1
            for d, a in sorted(rotten_in.items()):
                if d - day > 0 and a > 1:
                    eaten += 1
                    rotten_in[d] -= 1
                    break
        return eaten








tests = [
    ([1,2,3,5,2],   [3,2,1,4,2]),
    ([3,0,0,0,0,2], [3,0,0,0,0,2]),
]

for a, d in tests:
    print(Solution().eatenApples(a, d))
