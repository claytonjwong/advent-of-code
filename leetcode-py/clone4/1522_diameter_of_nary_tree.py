#
# 1522. Diameter of N-Ary Tree
#
# Q: https://leetcode.com/problems/diameter-of-n-ary-tree/
# A: https://leetcode.com/problems/diameter-of-n-ary-tree/discuss/755080/Javascript-Python3-C%2B%2B-post-order-traversal
#

class Solution:
    def diameter(self, root: 'Node', best = 0) -> int:
        def go(root, next = 0):
            nonlocal best
            if not root: # 🛑 base case
                return 0
            for child in root.children: # 🚀 DFS explore children
                cur = go(child)
                best = max(best, cur + next) # 🎯 best pair of current local maximums
                next = max(cur, next)
            return 1 + next # ⭐️ next candidate accumulated as the recursive stack unwinds
        go(root)
        return best
