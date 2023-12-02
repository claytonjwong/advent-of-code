#
# 104. Maximum Depth of Binary Tree
#
# Q: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# A: https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/955868/Kt-Js-Py3-Cpp-1-Liners
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
