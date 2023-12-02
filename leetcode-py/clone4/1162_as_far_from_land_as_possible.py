#
# 1162. As Far from Land as Possible
#
# Q: https://leetcode.com/problems/as-far-from-land-as-possible/
# A: https://leetcode.com/problems/as-far-from-land-as-possible/discuss/748163/Javascript-Python3-C%2B%2B-BFS-from-land-to-explore-water
#

class Solution:
    def maxDistance(self, A: List[List[int]]) -> int:
        N = len(A)
        q = collections.deque()
        seen = set()
        depth = 0
        for i in range(N):
            for j in range(N):
                if A[i][j]: # 🔍 init BFS queue with all 👀 seen land cells
                    q.append([ i, j ])
                    seen.add(f'{i},{j}')
        if len(q) == N * N:
            return -1 # ⭐️ edge case 1: no water
        while q:
            k = len(q)
            while k:
                i, j = q.popleft()
                for [u, v] in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]: # clockwise directions: [ 👆, 👉, 👇, 👈 ]
                    if not (u < 0 or u == N or v < 0 or v == N or A[u][v] or f'{u},{v}' in seen): # 🚌 BFS explore 👀 unseen water cells
                        q.append([ u, v ])
                        seen.add(f'{u},{v}')
                k -= 1
            depth += 1
        return depth - 1 # 🚌 BFS case: explored water from land, ending at max depth + 1 XOR ⭐️ edge case 2: no land
