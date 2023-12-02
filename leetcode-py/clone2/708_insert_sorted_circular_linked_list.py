#
# 708. Insert into a Sorted Circular Linked List
#
# Q: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# A: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/discuss/859467/Javascript-Python3-C%2B%2B-Simple-solutions
#

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', x: int) -> 'Node':
        alt = Node(x); alt.next = alt
        if not head:
            return alt
        big = head
        pre = head
        cur = head.next
        ok = lambda x: pre.val <= x <= cur.val
        while not ok(x) and cur != head:
            if big.val <= cur.val:
                big = cur
            pre = pre.next
            cur = cur.next
        if not ok(x):
            pre = big
            cur = big.next
        alt.next = cur
        pre.next = alt
        return head
