#
# 157. Read N Characters Given Read4
#
# Q: https://leetcode.com/problems/read-n-characters-given-read4/
# A: https://leetcode.com/problems/read-n-characters-given-read4/discuss/573173/Javascript-Python3-C%2B%2B-read-next-%2B-write-to-buf
#

class Solution:
    def read(self, buf, N, k = 0, write = 0):
        while True:
            next = [''] * 4
            k = read4(next)
            for i in range(0, k):
                if write < N:
                    buf[write] = next[i]; write += 1
            if k < 4 or write == N:
                return write
