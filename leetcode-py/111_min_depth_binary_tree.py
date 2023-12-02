#
# 111. Minimum Depth of Binary Tree
#
# Q: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# A: https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/553010/Kt-Js-Py3-Cpp-DFS-%2B-BFS
#

from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def go(node, depth = 1):
            if not node.left and not node.right:
                return depth
            L = go(node.left,  depth + 1) if node.left  else float('inf')
            R = go(node.right, depth + 1) if node.right else float('inf')
            return min(L, R)
        return go(root) if root else 0

# BFS
class Solution:
    def minDepth(self, root: TreeNode, depth = 1) -> int:
        if not root:
            return 0
        q = deque([ root ])
        while q:
            k = len(q)
            while k:
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left:  q.append(cur.left)
                if cur.right: q.append(cur.right)
                k -= 1
            depth += 1
        return -1
