#
# 701. Insert into a Binary Search Tree
#
# Q: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# A: https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/881995/Javascript-Python3-C%2B%2B-Recursive
#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# concise
class Solution:
    def insertIntoBST(self, root: TreeNode, x: int) -> TreeNode:
        def go(root, x):
            if x < root.val:
                root.left =  go(root.left, x)  if root.left  else TreeNode(x)
            else:
                root.right = go(root.right, x) if root.right else TreeNode(x)
            return root
        return go(root, x) if root else TreeNode(x)

# verbose
class Solution:
    def insertIntoBST(self, root: TreeNode, x: int) -> TreeNode:
        def go(root, x):
            if x < root.val:
                if root.left:
                    go(root.left, x)
                else:
                    root.left = TreeNode(x)
            else:
                if root.right:
                    go(root.right, x)
                else:
                    root.right = TreeNode(x)
            return root
        return go(root, x) if root else TreeNode(x)
