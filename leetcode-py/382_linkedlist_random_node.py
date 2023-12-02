#
# 382. Linked List Random Node
#
# Q: https://leetcode.com/problems/linked-list-random-node/
# A: https://leetcode.com/problems/linked-list-random-node/discuss/752830/Javascript-Python3-C%2B%2B-random-solutions
#

class Solution:
    def __init__(self, head: ListNode):
        self.head = head
        self.N = 0
        cur = head
        while cur:
            cur = cur.next
            self.N += 1
    def getRandom(self) -> int:
        cur = self.head
        hops = random.randint(0, self.N - 1)
        while hops:
            cur = cur.next
            hops -= 1
        return cur.val
