#
# 143. Reorder List
#
# Q: https://leetcode.com/problems/reorder-list/
# A: https://leetcode.com/problems/reorder-list/discuss/523554/Javascript-Python3-C%2B%2B-Stack-solutions
#

class Solution:
    def reorderList(self, head: ListNode) -> None:
        s = []
        beg = head
        while beg:
            s.append(beg)
            beg = beg.next
        half = len(s) // 2
        beg = head
        while half:
            end = s.pop()
            end.next = beg.next
            beg.next = end
            beg = end.next
            half -= 1
        if beg:
            beg.next = None
