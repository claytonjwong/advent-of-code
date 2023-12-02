#
# 510. Inorder Successor in BST II
#
# Q: https://leetcode.com/problems/inorder-successor-in-bst-ii/
# A: https://leetcode.com/problems/inorder-successor-in-bst-ii/discuss/848016/Javascript-Python3-C%2B%2B-Simple-solutions
#

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 1. left-most child of the node's right subtree
        c = node.right
        while c and c.left:
            c = c.left
        if c:
            return c
        # 2. closest parent with value greater-than the node's value
        p = node.parent
        while p and p.val < node.val:
            p = p.parent
        if p and node.val < p.val:
            return p
        # 3. none
        return None
