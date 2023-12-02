#
# 1721. Swapping Nodes in a Linked List
#
# Q: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# A: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1009772/Kt-Js-Py3-Cpp-Swap-based-upon-length-N
#

class Solution:
    def swapNodes(self, head: ListNode, K: int) -> ListNode:
        N, cur = 0, head
        while cur: cur = cur.next; N += 1
        i = K - 1
        j = N - K
        a = head
        b = head
        while i: a = a.next; i -= 1
        while j: b = b.next; j -= 1
        a.val, b.val = b.val, a.val
        return head
