#
# 203. Remove Linked List Elements
#
# Q: https://leetcode.com/problems/remove-linked-list-elements/
# A: https://leetcode.com/problems/remove-linked-list-elements/discuss/745857/Javascript-Python3-C%2B%2B-iterative-with-sentinel
#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, T: int) -> ListNode:
        sentinel = ListNode(-1, head)
        pre, cur = sentinel, head
        while True:
            print('cur: ' + str(cur.val) + ' , pre: ' + str(pre.val))
            if cur and cur.val == T:
                cur = cur.next
            pre.next = cur
            pre = pre.next
            if not cur:
                break
            cur = cur.next
        return sentinel.next
