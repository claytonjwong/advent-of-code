#
# 67. Add Binary
#
# Q: https://leetcode.com/problems/add-binary/
# A: https://leetcode.com/problems/add-binary/discuss/744220/Javascript-Python3-C%2B%2B-accumulate-sum-a%2Bb%2Bc-in-reverse
#

class Solution:
    def addBinary(self, A: str, B: str, c = 0) -> str: # ⭐️ c is the carry
        ans = []
        i = len(A) - 1
        j = len(B) - 1
        while 0 <= i or 0 <= j:
            a = int(A[i]) if 0 <= i else 0
            b = int(B[j]) if 0 <= j else 0
            ans.append((a + b + c) % 2)
            c = 1 < a + b + c
            i -= 1
            j -= 1
        if c:
            ans.append(1)
        ans.reverse()
        return ''.join(list(map(lambda x: str(x), ans)))
