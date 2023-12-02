#
# 61. Rotate List
#
# Q: https://leetcode.com/problems/rotate-list/
# A: https://leetcode.com/problems/rotate-list/discuss/152985/Javascript-Python3-C%2B%2B-Self-Documented
#

from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, oldHead: ListNode, K: int, N = 0) -> ListNode:
        it = oldHead
        while it:
            N += 1
            it = it.next
        rotate = K % N if N else 0
        if not rotate:
            return oldHead
        tail = ListNode(-1, oldHead)
        pivot = N - rotate
        while pivot:
            pivot -= 1
            tail = tail.next
        newHead = tail.next; tail.next = None
        tail = newHead
        while tail.next:
            tail = tail.next
        tail.next = oldHead
        return newHead
