#
#  938. Range Sum of BST
#
# Q: https://leetcode.com/problems/range-sum-of-bst/
# A: https://leetcode.com/problems/range-sum-of-bst/discuss/192070/Kt-Js-Py3-Cpp-solutions
#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, lo: int, hi: int) -> int:
        if not root:
            return 0
        x = root.val if lo <= root.val <= hi else 0
        return x + self.rangeSumBST(root.left, lo, hi) + self.rangeSumBST(root.right, lo, hi)
