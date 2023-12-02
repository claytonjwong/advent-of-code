#
# 1602. Find Nearest Right Node in Binary Tree
#
# Q: https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
# A: https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/discuss/875464/Javascript-Python3-C%2B%2B-DFS-and-BFS
#

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def findNearestRightNode(self, root: TreeNode, T: TreeNode, found = -1) -> TreeNode:
        def go(node = root, depth = 0):
            nonlocal found
            if not node:
                return None
            if depth == found:
                return node
            if node == T:
                found = depth
            L = go(node.left,  depth + 1)
            R = go(node.right, depth + 1)
            return L if L else R if R else None
        return go()

# BFS
class Solution:
    def findNearestRightNode(self, root: TreeNode, T: TreeNode) -> TreeNode:
        q = deque([ root ])
        while len(q):
            next = deque()
            while len(q):
                node = q.popleft()
                if node == T:
                    return q[0] if len(q) else None
                if node.left:  next.append(node.left)
                if node.right: next.append(node.right)
            [q, next] = [next, q]
        return None
