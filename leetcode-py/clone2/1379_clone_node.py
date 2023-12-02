#
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#
# Q: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# A: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/discuss/537655/Kt-Js-Py3-Cpp-Traverse-A%2BB-Simultaneously
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, A: TreeNode, B: TreeNode, T: TreeNode) -> TreeNode:
        def go(a, b):
            if a == T:
                return b
            L = go(a.left, b.left)   if a.left  else None
            R = go(a.right, b.right) if a.right else None
            return L if L else R
        return go(A, B)
