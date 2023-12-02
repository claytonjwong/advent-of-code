#
# 1506. Find Root of N-Ary Tree
#
# Q: https://leetcode.com/problems/find-root-of-n-ary-tree/
# A: https://leetcode.com/problems/find-root-of-n-ary-tree/discuss/729168/Kt-Js-Py3-Cpp-O(N)-%2B-O(1)-memory-solutions
#

# naive
class Solution:
    def findRoot(self, A: List['Node']) -> 'Node':
        children = set()
        for it in A:
            [children.add(child) for child in it.children]
        return [it for it in A if it not in children][0]

# memory optimized
class Solution:
    def findRoot(self, A: List['Node'], x = 0) -> 'Node':
        for it in A:
            x ^= it.val
            for child in it.children:
                x ^= child.val
        return [it for it in A if x == it.val][0]
