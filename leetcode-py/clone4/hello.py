from collections import deque
from typing import List
class Solution:
    def minimumMoves(self, A: List[List[int]], N = 3, INF = int(1e9 + 7), t = 0) -> int:
        for i in range(N):
            for j in range(N):
                if A[i][j] <= 1:
                    continue
                q, seen, depth = deque([(i, j)]), set([(i, j)]), 0
                take = A[i][j] - 1
                while True:
                    for _ in range(len(q)):
                        i, j = q.popleft()
                        if not A[i][j]:
                            A[i][j] = 1; take -= 1; t += depth
                            print(f'set A[{i}][{j}] = 1   take: {take}  t += {depth} = {t}')
                        if not take:
                            break
                        for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                            if 0 <= u < N and 0 <= v < N and (u, v) not in seen:
                                q.append((u, v)); seen.add((u, v))
                    depth += 1
        return t

s = Solution()
print(s.minimumMoves([[3,2,0],[0,1,0],[0,3,0]]))
