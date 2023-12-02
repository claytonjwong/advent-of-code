#
# 1457. Pseudo-Palindromic Paths in a Binary Tree
#
# Q: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# A: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/652445/Kt-Js-Py3-Cpp-Map
#

from collections import Counter

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode, odd = 0, paths = 0) -> int:
        m = Counter()
        def go(root):
            nonlocal odd, paths
            x = root.val
            m[x] += 1; odd += 1 if m[x] & 1 else -1
            if not root.left and not root.right:
                paths += odd <= 1
            if root.left:  go(root.left)
            if root.right: go(root.right)
            m[x] -= 1; odd += 1 if m[x] & 1 else -1
        go(root)
        return paths
