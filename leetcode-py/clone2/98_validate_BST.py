#
# 98. Validate Binary Search Tree
#
# Q: https://leetcode.com/problems/validate-binary-search-tree/
# A: https://leetcode.com/problems/validate-binary-search-tree/discuss/116826/Kt-Js-Py3-Cpp-Recursive
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, lo = -float('inf'), hi = float('inf')) -> bool:
        if not root:
            return True
        if root.val <= lo or hi <= root.val:
            return False
        return self.isValidBST(root.left, lo, root.val) and self.isValidBST(root.right, root.val, hi)
