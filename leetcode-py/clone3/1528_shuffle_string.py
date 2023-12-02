#
# 1528. Shuffle String
#
# Q: https://leetcode.com/problems/shuffle-string/
# A: https://leetcode.com/problems/shuffle-string/discuss/756041/Javascript-Python3-C%2B%2B-create-t-from-s
#
class Solution:
    def restoreString(self, s: str, A: List[int]) -> str:
        return ''.join(map(lambda pair: pair[1], sorted(zip(A, s))))

class Solution:
    def restoreString(self, s: str, A: List[int]) -> str:
        N = len(A)
        t = ['\0'] * N
        for i in range(N):
            t[A[i]] = s[i]
        return ''.join(t)
