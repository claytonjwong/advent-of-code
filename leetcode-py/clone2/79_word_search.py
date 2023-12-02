#
# 79. Word Search
#
# Q: https://leetcode.com/problems/word-search/
# A: https://leetcode.com/problems/word-search/discuss/747545/Javascript-Python3-C%2B%2B-DFS-%2B-BT
#

class Solution:
    def exist(self, A: List[List[str]], T: str) -> bool:
        M = len(A);
        N = len(A[0])
        path, seen = [], set()
        def go(i, j):
            # 🛑 OOB, char mismatch, or already seen
            if i < 0 or i == M or j < 0 or j == N or A[i][j] != T[len(path)] or f'{i},{j}' in seen:
                return False
            # 🚀 DFS + BT
            path.append(A[i][j]), seen.add(f'{i},{j}') # 👀 path seen ✅ forward-tracking
            if len(path) == len(T):
                return True # ⭐️ path == target T 🎯
            for [u, v] in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]: # clockwise directions: [ 👆, 👉, 👇, 👈 ]
                if (go(u, v)):
                    return True
            path.pop(), seen.remove(f'{i},{j}')        # 👀 path seen 🚫 back-tracking
        for i in range(M):
            for j in range(N):
                if (go(i, j)):
                    return True
        return False
