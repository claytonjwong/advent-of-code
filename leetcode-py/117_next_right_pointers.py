#
# 117. Populating Next Right Pointers in Each Node II
#
# Q: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# A: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/706949/Kt-Js-Py3-Cpp-BFS
#

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root]) if root else None
        while q:
            k = len(q)
            while k:
                cur = q.popleft(); k -= 1
                cur.next = q[0] if k else None
                if cur.left:  q.append(cur.left)
                if cur.right: q.append(cur.right)
        return root
