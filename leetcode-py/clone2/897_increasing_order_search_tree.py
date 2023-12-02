#
# 897. Increasing Order Search Tree
#
# Q: https://leetcode.com/problems/increasing-order-search-tree/
# A: https://leetcode.com/problems/increasing-order-search-tree/discuss/165898/Kt-Js-Py3-Cpp-solutions
#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        A = []
        def go(root):
            if not root:
                return
            go(root.left)
            A.append(root)
            go(root.right)
            root.left = root.right = None
        go(root)
        sentinel = TreeNode(-1)
        cur = sentinel
        for root in A:
            cur.right = root
            cur = cur.right
        return sentinel.right
