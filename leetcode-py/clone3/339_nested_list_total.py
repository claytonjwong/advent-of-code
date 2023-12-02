#
# 339. Nested List Weight Sum
#
# Q: https://leetcode.com/problems/nested-list-weight-sum/
# A: https://leetcode.com/problems/nested-list-weight-sum/discuss/124490/Kt-Js-Py3-Cpp-Recursive
#

class Solution:
    def depthSum(self, A: List[NestedInteger], depth = 1, total = 0) -> int:
        for it in A:
            if it.isInteger():
                total += it.getInteger() * depth
            else:
                total += self.depthSum(it.getList(), depth + 1)
        return total
