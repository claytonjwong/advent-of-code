#
# 1291. Sequential Digits
#
# Q: https://leetcode.com/problems/sequential-digits/
# A: https://leetcode.com/problems/sequential-digits/discuss/455969/Javascript-and-C%2B%2B-solutions
#

class Solution:
    def sequentialDigits(self, lo: int, hi: int) -> List[int]:
        ans = []
        def go(x):
            if hi < x:
                return
            if lo <= x:                  # 🎯 lo <= x <= hi
                ans.append(x)
            last = x % 10
            next = last + 1
            if next < 10:
                go(x * 10 + next)
        [ go(i) for i in range(1, 10) ]
        return sorted(ans)
