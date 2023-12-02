#
# 1026. Maximum Difference Between Node and Ancestor
#
# Q: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# A: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/390492/Kt-Js-Py3-Cpp-Pre-Order-Traversal
#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def go(root, lo, hi):
            if not root:
                return abs(lo - hi)
            lo = min(lo, root.val)
            hi = max(hi, root.val)
            return max(go(root.left, lo, hi), go(root.right, lo, hi))
        return go(root, root.val, root.val)
