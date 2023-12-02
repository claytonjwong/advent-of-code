#
# 82. Remove Duplicates from Sorted List II
#
# Q: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# A: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/590900/Kt-Js-Py3-Cpp-Single-Pass
#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(-123, head)
        ans = sentinel
        pre = head
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre == cur:
                ans.next = cur; ans = ans.next
            cur = cur.next; pre = cur
        ans.next = None
        return sentinel.next
