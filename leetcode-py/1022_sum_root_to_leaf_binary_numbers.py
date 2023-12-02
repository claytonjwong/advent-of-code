#
# 1022. Sum of Root To Leaf Binary Numbers
#
# Q: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# A: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/275849/Javascript-Python3-C%2B%2B-recursive-solutions
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode, sum = 0) -> int:
        next = lambda sum: (sum << 1) | root.val
        if not root: return 0
        if not root.left and not root.right: return next(sum)
        return self.sumRootToLeaf(root.left, next(sum)) + self.sumRootToLeaf(root.right, next(sum))
