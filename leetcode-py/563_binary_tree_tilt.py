#
# 563. Binary Tree Tilt
#
# Q: https://leetcode.com/problems/binary-tree-tilt/
# A: https://leetcode.com/problems/binary-tree-tilt/discuss/928266/Kt-Js-Py3-Cpp-Post-Order-Traversal
#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode, total = 0) -> int:
        def go(root):
            nonlocal total
            if not root:
                return 0
            L = go(root.left)
            R = go(root.right)
            total += abs(L - R)
            return root.val + L + R
        go(root)
        return total
