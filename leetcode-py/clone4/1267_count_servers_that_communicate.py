#
# 1267. Count Servers that Communicate
#
# Q: https://leetcode.com/problems/count-servers-that-communicate/
# A: https://leetcode.com/problems/count-servers-that-communicate/discuss/438394/Javascript-Python3-C%2B%2B-Count-per-Row-and-Column
#

from typing import List

class Solution:
    def countServers(self, A: List[List[int]], cnt = 0) -> int:
        M = len(A)
        N = len(A[0])
        row = [0] * M
        col = [0] * N
        servers = []
        for i in range(M):
            for j in range(N):
                if A[i][j]:
                    row[i] += 1
                    col[j] += 1
                    servers.append([ i, j ])
        for [i, j] in servers:
            if 1 < row[i] or 1 < col[j]:
                cnt += 1
        return cnt
