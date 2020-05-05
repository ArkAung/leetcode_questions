from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or A is None:
            return 0
        rows = len(A)
        cols = len(A[0])
        if cols % 2 == 0:
            half_cols = cols//2
        else:
            half_cols = (cols//2) +1
        for r in range(rows):
            for c in range(half_cols):
                A[r][c], A[r][cols - c -1] = 1-A[r][cols - c -1], 1-A[r][c]
        return A
