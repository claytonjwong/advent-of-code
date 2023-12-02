#
# 337. House Robber III
#
# Q: https://leetcode.com/problems/house-robber-iii/
# A: https://leetcode.com/problems/house-robber-iii/discuss/946524/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def rob(self, root: TreeNode) -> int:
        def go(root, isRobbable = True):
            if not root:
                return 0
            include = go(root.left, False) + go(root.right, False) + root.val
            exclude = go(root.left, True)  + go(root.right, True)
            return max(include if isRobbable  else -float('inf'), exclude)
        return go(root)

# Memo
class Solution:
    def rob(self, root: TreeNode) -> int:
        m = {}
        def go(root, isRobbable = True):
            key = f'{root},{isRobbable}'
            if key in m:
                return m[key]
            if not root:
                m[key] = 0
                return m[key]
            include = go(root.left, False) + go(root.right, False) + root.val
            exclude = go(root.left, True)  + go(root.right, True)
            m[key] = max(include if isRobbable else -float('inf'), exclude)
            return m[key]
        return go(root)
