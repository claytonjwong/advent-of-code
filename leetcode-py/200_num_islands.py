#
# 200. Number of Islands
#
# Q: https://leetcode.com/problems/number-of-islands/
# A: https://leetcode.com/problems/number-of-islands/discuss/753546/Javascript-Python3-C%2B%2B-DFS-%2B-BFS
#

# DFS
class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        seen = set()
        M = len(A)
        N = len(A[0]) if M else 0
        def go(i, j):
            if i < 0 or i == M or j < 0 or j == N or A[i][j] == '0' or f'{i},{j}' in seen: # 🛑 OOB, water, or already seen 
                return 0
            seen.add(f'{i},{j}')
            for [u, v] in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]: # 🚀 DFS explore adj u,v [👆, 👉, 👇, 👈]
                go(u, v)
            return 1
        return sum(go(i, j) for i in range(M) for j in range(N))

# BFS
class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        seen = set()
        M = len(A)
        N = len(A[0]) if M else 0
        def bfs(row, col):
            if A[row][col] == '0' or f'{row},{col}' in seen: # 🚫 water or already seen 👀
                return 0
            seen.add(f'{row},{col}')
            q = collections.deque([[ row, col ]])
            while q: # for each i,j 🚌 BFS explore adj u,v [👆, 👉, 👇, 👈] if *not* 🛑 OOB, 🚫 water, or already seen 👀
                i, j = q.popleft()
                seen.add(f'{i},{j}')
                for u, v in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
                    if not (u < 0 or u == M or v < 0 or v == N or A[u][v] == '0' or f'{u},{v}' in seen):
                        q.append([ u, v ])
                        seen.add(f'{u},{v}')
            return 1
        return sum(bfs(i, j) for i in range(M) for j in range(N))
