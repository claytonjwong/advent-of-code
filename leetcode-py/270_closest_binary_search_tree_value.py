#
# 270. Closest Binary Search Tree Value
#
# Q: https://leetcode.com/problems/closest-binary-search-tree-value/
# A: https://leetcode.com/problems/closest-binary-search-tree-value/discuss/549446/Javascript-and-C%2B%2B-solutions
#

class Solution:
    def closestValue(self, root: TreeNode, T: float, best = float('inf')) -> int:
        def go(root):
            nonlocal best
            if not root:
                return 0
            if abs(root.val - T) < abs(best - T):
                best = root.val
            go(root.left)
            go(root.right)
        go(root)
        return best
