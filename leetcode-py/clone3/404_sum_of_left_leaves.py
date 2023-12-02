#
# 404. Sum of Left Leaves
#
# Q: https://leetcode.com/problems/sum-of-left-leaves/
# A: https://leetcode.com/problems/sum-of-left-leaves/discuss/809409/Javascript-Python3-C%2B%2B-1-Liners
#

# 1-liner
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, left = False) -> int:
        return 0 if not root else (root.val if left else 0) if not root.left and not root.right else self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)

# verbose
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, left = False) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if left else 0
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
