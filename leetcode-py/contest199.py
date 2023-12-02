#
# Contest: https://leetcode.com/contest/weekly-contest-199
# Screenshare: https://www.youtube.com/watch?v=ufTyfhb0wQY&feature=youtu.be
#
# Rank            Name             Score    Finish Time    Q1 (3)     Q2 (4)        Q3 (5)     Q4 (8)
# 6247 / 14309    claytonjwong     7        0:32:15        0:04:16    0:27:15 *1
#

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

#
# 1529. Bulb Switcher IV
#
# Q: https://leetcode.com/problems/bulb-switcher-iv/
# A: https://leetcode.com/problems/bulb-switcher-iv/discuss/755780/Javascript-Python3-C%2B%2B-count-bit-flips
#
class Solution:
    def minFlips(self, s: str, cur = '0', cnt = 0) -> int:
        for c in s:
            if cur != c:
                cur = c
                cnt += 1
        return cnt
