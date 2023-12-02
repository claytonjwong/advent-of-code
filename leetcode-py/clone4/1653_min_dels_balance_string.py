#
# 1653. Minimum Deletions to Make String Balanced
#
# Q: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# A: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/938408/Kt-Js-Py3-Cpp-Prefix-%2B-Suffix
#

class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        prefix = [0] * N
        suffix = [0] * N
        for i in range(N):             prefix[i] = int(s[i] == 'b') + (prefix[i - 1] if 0 < i     else 0)
        for i in range(N - 1, -1, -1): suffix[i] = int(s[i] == 'a') + (suffix[i + 1] if i < N - 1 else 0)
        return min(a + b for a, b in zip(prefix, suffix)) - 1  # ⭐️ -1 since we only need to delete 'a' xor 'b' at the optimal "pivot" index
