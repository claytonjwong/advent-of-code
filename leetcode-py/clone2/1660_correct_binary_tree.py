#
# 1660. Correct a Binary Tree
#
# Q: https://leetcode.com/problems/correct-a-binary-tree/
# A: https://leetcode.com/problems/correct-a-binary-tree/discuss/943193/Kt-Js-Py3-Cpp-Map-%2B-Seen-solutions
#

# map
class Solution:
    def correctBinaryTree(self, root: TreeNode, found = False) -> TreeNode:
        m = {}
        def go(root):
            nonlocal found
            if root in m:
                target = m[root]
                parent = m[target]
                if parent.left  == target: parent.left  = None
                if parent.right == target: parent.right = None
                found = True
                return None
            if not found and root.left:  go(root.left);  m[root.left]  = root
            if not found and root.right: go(root.right); m[root.right] = root
            return root
        return go(root)

# seen
class Solution:
    def correctBinaryTree(self, root: TreeNode, found = False) -> TreeNode:
        seen = set()
        def go(root):
            nonlocal found
            seen.add(root)
            if root.right in seen:
                found = True
                return None
            if not found and root.right: root.right = go(root.right)
            if not found and root.left:  root.left  = go(root.left)
            return root
        return go(root)
