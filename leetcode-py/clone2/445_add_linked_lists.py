#
# 445. Add Two Numbers II
#
# Q: https://leetcode.com/problems/add-two-numbers-ii/
# A: https://leetcode.com/problems/add-two-numbers-ii/discuss/927269/Kt-Js-Py3-Cpp-Recursive-Reverse
#

class ListNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, A: ListNode, B: ListNode) -> ListNode:
        def rev(cur: ListNode, pre: ListNode = None) -> ListNode:
            if not cur.next:
                cur.next = pre
                return cur
            next = cur.next
            cur.next = pre
            return rev(next, cur)
        a = rev(A)
        b = rev(B)
        ans = ListNode(-1)
        cur = ans
        carry = 0
        while a or b:
            c = (a.val if a else 0) + (b.val if b else 0) + carry
            carry = 1 if 10 <= c else 0; c %= 10
            cur.next = ListNode(c); cur = cur.next
            if a: a = a.next
            if b: b = b.next
        if carry:
            cur.next = ListNode(1)
        return rev(ans.next)
