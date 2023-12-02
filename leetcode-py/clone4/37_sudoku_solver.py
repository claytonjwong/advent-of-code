from typing import List

class Solution:
    def solveSudoku(self, A: List[List[str]], N = 9) -> None:
        def ok(i, j):
            row, col, box = set(), set(), set()
            for k in range(N):
                if A[i][k] != '.' and A[i][k] in row:
                    return False
                else:
                    row.add(A[i][k])
            for k in range(N):
                if A[k][j] != '.' and A[k][j] in col:
                    return False
                else:
                    col.add(A[k][j])
            i = 3 * (i // 3)
            j = 3 * (j // 3)
            for u in range(i, i + 3):
                for v in range(j, j + 3):
                    if A[u][v] != '.' and A[u][v] in box:
                        return False
                    else:
                        box.add(A[u][v])
            return True
        def go():
            for i in range(N):
                for j in range(N):
                    if A[i][j] != '.':
                        continue
                    for k in range(1, N + 1):
                        A[i][j] = f'{k}'
                        if ok(i, j) and go():
                            return True
                        A[i][j] = '.'
                    return False
            return True
        go()

A = [['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.'],
     ['.','.','.','.','.','.','.','.','.']]
Solution().solveSudoku(A)
for row in A:
    print(row)

# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['4', '5', '6', '7', '8', '9', '1', '2', '3']
# ['7', '8', '9', '1', '2', '3', '4', '5', '6']
# ['2', '1', '4', '3', '6', '5', '8', '9', '7']
# ['3', '6', '5', '8', '9', '7', '2', '1', '4']
# ['8', '9', '7', '2', '1', '4', '3', '6', '5']
# ['5', '3', '1', '6', '4', '2', '9', '7', '8']
# ['6', '4', '2', '9', '7', '8', '5', '3', '1']
