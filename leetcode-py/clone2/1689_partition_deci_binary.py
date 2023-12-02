#
# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
#
# Q: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# A: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/discuss/970252/Kt-Js-Py3-Cpp-1-Liners
#

class Solution:
    def minPartitions(self, s: str) -> int:
        return max(int(c) for c in s)
