#
# 2. Add Two Numbers
#
# Q: https://leetcode.com/problems/add-two-numbers/
# A: https://leetcode.com/problems/add-two-numbers/discuss/1093/Kt-Js-Py3-Cpp-Concise-solutions
#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, A: ListNode, B: ListNode, carry = False) -> ListNode:
        ans = ListNode(-1)
        cur = ans
        while A or B or carry:
            a = A.val if A else 0
            b = B.val if B else 0
            c = a + b + (1 if carry else 0)
            carry = 10 <= c; c %= 10
            cur.next = ListNode(c); cur = cur.next
            A = A.next if A else None
            B = B.next if B else None
        return ans.next
