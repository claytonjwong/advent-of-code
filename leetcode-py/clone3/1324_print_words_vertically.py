#
# 1324. Print Words Vertically
#
# Q: https://leetcode.com/problems/print-words-vertically/
# A: https://leetcode.com/problems/print-words-vertically/discuss/485298/Javascript-Python3-C%2B%2B-Straightforward-solutions
#

class Solution:
    def printVertically(self, s: str) -> List[str]:
        A = s.split(' ')
        N = len(A)
        K = max([ len(word) for word in A ])
        A = [word.ljust(K) for word in A]
        ans = []
        for j in range(K):
            word = []
            for i in range(N):
                word.append(A[i][j])
            ans.append(''.join(word).rstrip())
        return ans
