#
# 369. Plus One Linked List
#
# Q: https://leetcode.com/problems/plus-one-linked-list/
# A: https://leetcode.com/problems/plus-one-linked-list/discuss/973286/Kt-Js-Py3-Cpp-Recursive-solutions
#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def go(node):
            if not node:
                return False
            carry = go(node.next)
            if carry or not node.next:
                node.val += 1
            if node.val == 10:
                node.val = 0
                return True
            return False
        if go(head):
            pre = ListNode(1)
            pre.next = head
            return pre
        return head
