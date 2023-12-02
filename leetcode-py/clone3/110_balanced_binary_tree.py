#
# 110. Balanced Binary Tree
#
# Q: https://leetcode.com/problems/balanced-binary-tree/
# A: https://leetcode.com/problems/balanced-binary-tree/discuss/981963/Kt-Js-Py3-Cpp-Post-Order-Traversal
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode, ok = True) -> bool:
        def go(root):
            nonlocal ok
            if not root:
                return 0
            L = 1 + go(root.left)
            R = 1 + go(root.right)
            if 1 < abs(L - R):
                ok = False
            return max(L, R)
        go(root)
        return ok
