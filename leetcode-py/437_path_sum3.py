#
# 437. Path Sum III
#
# Q: https://leetcode.com/problems/path-sum-iii/
# A: https://leetcode.com/problems/path-sum-iii/discuss/671026/Javascript-Python3-C%2B%2B-solutions
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, T: int) -> int:
        def go(root, sum = 0):
            if not root:
                return 0
            sum += root.val
            return int(sum == T) + go(root.left, sum) + go(root.right, sum)
        def traverse(root):
            if not root:
                return 0
            return go(root) + traverse(root.left) + traverse(root.right)
        return traverse(root)
