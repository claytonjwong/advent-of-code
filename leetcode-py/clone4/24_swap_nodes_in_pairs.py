#
# 24. Swap Nodes in Pairs
#
# Q: https://leetcode.com/problems/swap-nodes-in-pairs/
# A: https://leetcode.com/problems/swap-nodes-in-pairs/discuss/759536/Javascript-Python3-C%2B%2B-sliding-window%3A-a-b-c
#

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        a = ListNode(-1, head)
        b = head
        c = head.next if head else None
        if not c:
            return head
        head = c
        while True:
            d = c.next # ⭐️ d is the beginning of the next pair to swap
            a.next = c
            b.next = c.next
            c.next = b
            if not d or not d.next: # ❌ nothing left to swap
                break
            a = b
            b = d
            c = d.next
        return head
