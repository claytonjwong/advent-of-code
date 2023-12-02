#
# 449. Serialize and Deserialize BST
#
# Q: https://leetcode.com/problems/serialize-and-deserialize-bst/
# A: https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93191/Javascript-Python3-C%2B%2B-Recursive-Pre-Order-Traversal
#

class TreeNode:
    def __init__(self, val = 0, left = None, right = None)
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        q = []
        def go(root):
            if not root:
                q.append(-1)
                return
            q.append(root.val)
            go(root.left)
            go(root.right)
        go(root)
        return ' '.join([str(x) for x in q])

    def deserialize(self, data: str) -> TreeNode:
        q = deque([int(s) for s in data.split(' ')])
        def go():
            if not len(q):
                return
            x = q.popleft()
            root = TreeNode(x) if -1 < x else None
            if root: root.left  = go()
            if root: root.right = go()
            return root
        return go()
