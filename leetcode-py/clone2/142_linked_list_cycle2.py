#
# 142. Linked List Cycle II
#
# Q: https://leetcode.com/problems/linked-list-cycle-ii/
# A: https://leetcode.com/problems/linked-list-cycle-ii/discuss/523559/Kt-Js-Py3-Cpp-Seen-ListNodes
#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
