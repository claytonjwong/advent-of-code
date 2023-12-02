#
# 1120. Maximum Average Subtree
#
# Q: https://leetcode.com/problems/maximum-average-subtree/
# A: https://leetcode.com/problems/maximum-average-subtree/discuss/765869/Javascript-Python3-C%2B%2B-post-order-traversal
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode, best = 0) -> float:
        def go(root):
            nonlocal best
            if not root:
                return [0, 0]
            L, M = go(root.left)
            R, N = go(root.right)
            total = root.val + L + R
            cnt = 1 + M + N  # +1 for current node
            best = max(best, total / cnt)
            return [total, cnt]
        go(root)
        return best
