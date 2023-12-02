#
# 669. Trim a Binary Search Tree
#
# Q: https://leetcode.com/problems/trim-a-binary-search-tree/
# A: https://leetcode.com/problems/trim-a-binary-search-tree/discuss/599189/Javascript-Python3-C%2B%2B-Recursive
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# concise
class Solution:
    def trimBST(self, root: TreeNode, lo: int, hi: int) -> TreeNode:
        def go(root):
            while root.left  and root.left.val < lo:  root.left  = root.left.right if root.left.right else None
            while root.right and hi < root.right.val: root.right = root.right.left if root.right.left else None
            if root.left:  go(root.left)
            if root.right: go(root.right)
        go(root)
        while root and root.val < lo: root = root.right
        while root and hi < root.val: root = root.left
        return root

# verbose
class Solution:
    def trimBST(self, root: TreeNode, lo: int, hi: int) -> TreeNode:
        def go(root):
            if root.left and root.left.val < lo:
                next = root.left.right
                while next and next.val < lo:
                    next = next.right
                root.left = next
            if root.right and hi < root.right.val:
                next = root.right.left
                while next and hi < next.val:
                    next = next.left
                root.right = next
            if root.left:  go(root.left)
            if root.right: go(root.right)
        go(root)
        while root and root.val < lo: root = root.right
        while root and hi < root.val: root = root.left
        return root
