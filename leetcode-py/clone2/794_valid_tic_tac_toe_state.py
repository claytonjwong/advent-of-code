#
# 794. Valid Tic-Tac-Toe State
#
# Q: https://leetcode.com/problems/valid-tic-tac-toe-state/
# A: https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/117603/Javascript-Python3-C%2B%2B-Concise-solutions
#

from typing import List

class Solution:
    def validTicTacToe(self, A: List[str], winX = False, winO = False) -> bool:
        X = sum([row.count('X') for row in A])
        O = sum([row.count('O') for row in A])
        def win(c):
            target = c * 3
            for row in A:
                if row == target: return True
            for j in range(3):
                col = A[0][j] + A[1][j] + A[2][j]
                if col == target: return True
            return A[0][0] + A[1][1] + A[2][2] == target or A[0][2] + A[1][1] + A[2][0] == target
        winX = win('X')
        winO = win('O')
        if winX and winO:       return False  # case 1: if X won and O won
        if winX and X - O != 1: return False  # case 2: if X won, then there must be one more X than O
        if winO and X - O != 0: return False  # case 3: if O won, then there must be the same amount of X and O
        return X - O in [0, 1]                # case 4: if no winner, then there must be the same amount of X and O xor one more X than O
