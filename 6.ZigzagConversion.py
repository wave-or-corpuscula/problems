# https://leetcode.com/problems/zigzag-conversion/description/


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         result = [list() for _ in range(numRows)]
#         i = 0
#         down = True
#         row_track = 0
#         while i < len(s):
#             if row_track in tuple(range(0, numRows)):
#                 result[row_track].append(s[i])
#                 if down:
#                     row_track += 1
#                 else:
#                     row_track -= 1
#                 i += 1
#                 continue

#             if row_track == numRows:
#                 row_track -= 2
#                 down = False
#             elif row_track == -1:
#                 row_track = 1
#                 down = True

#         for row in result:
#             print(row)
#         return "".join("".join(row) for row in result)



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [list() for _ in range(numRows)]
        i = 0
        down = True
        row_track = 0
        while i < len(s):
            if row_track in tuple(range(0, numRows)):
                result[row_track].append(s[i])
                if down:
                    row_track += 1
                else:
                    row_track -= 1
                i += 1
                continue

            if row_track == numRows:
                row_track -= 2
                down = False
            elif row_track == -1:
                row_track = 1
                down = True
        return "".join("".join(row) for row in result)
    

class BestSolution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr_row = 0
        going_down = False

        for c in s:
            rows[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        return ''.join(rows)


if __name__ == "__main__":
    sol = BestSolution()
    tests = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
    ]
    for test in tests:
        print(sol.convert(*test))