#
# 1586. Binary Search Tree Iterator II
#
# Q: https://leetcode.com/problems/binary-search-tree-iterator-ii/
# A: https://leetcode.com/problems/binary-search-tree-iterator-ii/discuss/852792/Javascript-Python3-C%2B%2B-Naive-solutions
#

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.A = []
        self.i = -1
        def go(root):
            if not root:
                return
            go(root.left)
            self.A.append(root.val)
            go(root.right)
        go(root)

    def hasPrev(self) -> bool: return 0 < self.i
    def hasNext(self) -> bool: return self.i + 1 < len(self.A)

    def next(self) -> int: self.i += 1; return self.A[self.i]
    def prev(self) -> int: self.i -= 1; return self.A[self.i]
