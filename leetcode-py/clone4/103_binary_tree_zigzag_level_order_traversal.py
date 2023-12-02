#
# 103. Binary Tree Zigzag Level Order Traversal
#
# Q: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# A: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/749264/Javascript-Python3-C%2B%2B-BFS-per-Level
#

class Solution:
    def zigzagLevelOrder(self, root: TreeNode, rev = 0) -> List[List[int]]:
        ans = []
        q = collections.deque([ root ]) if root else None
        while q:
            ans.append(list(map(lambda node: node.val, q)))
            if rev:
                ans[-1].reverse()
            k = len(q)
            for _ in range(k):
                cur = q.popleft()
                if cur.left:  q.append(cur.left)
                if cur.right: q.append(cur.right)
            rev ^= 1
        return ans
