#
# 338. Counting Bits
#
# Q: https://leetcode.com/problems/counting-bits/
# A: https://leetcode.com/problems/counting-bits/discuss/657068/Kt-Js-Py3-Cpp-Dynamic-Programming
#

class Solution:
    def countBits(self, N: int) -> List[int]:
        ans = [ 0 ]
        for i in range(1, N + 1):
            ans.append(ans[i >> 1] + (i & 1))
        return ans
