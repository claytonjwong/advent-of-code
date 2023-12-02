#
# 431. Encode N-ary Tree to Binary Tree
#
# Q: https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# A: https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/discuss/920789/Kt-Js-Py3-Cpp-Recursive-Copy
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val = 0, children = None):
        self.val = val
        self.children = children.copy()

class Codec:
    def encode(self, parent: 'Node') -> TreeNode:
        if not parent:
            return None
        copy = TreeNode(parent.val)
        next = None
        for child in parent.children:
            if next:
                next.right = self.encode(child)
                next = next.right
            else:
                copy.left = self.encode(child)
                next = copy.left
        return copy

    def decode(self, parent: TreeNode) -> 'Node':
        if not parent:
            return None
        copy = Node(parent.val, [])
        next = parent.left
        while next:
            copy.children.append(self.decode(next))
            next = next.right
        return copy
