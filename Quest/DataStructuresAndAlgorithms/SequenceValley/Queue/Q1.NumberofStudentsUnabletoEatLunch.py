# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=problem-list-v2&envId=dsa-sequence-valley-queue

from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        rounds = 0
        while sandwiches and rounds <= len(students):
            print(students)
            student = students.pop(0)
            if student != sandwiches[0]:
                students.append(student)
                rounds += 1
                continue

            sandwiches.pop(0)
            rounds = 0
        
        return len(students)
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,0,0],     [0,1,0,1]),
        ([1,1,1,0,0,1], [1,0,0,0,1,1]),
    ]
    for stud, sand in tests:
        res = sol.countStudents(stud, sand)
        print(res)
            