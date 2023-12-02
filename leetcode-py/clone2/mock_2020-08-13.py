#
# Google- Phone Interview
# Completed August 13, 2020 4:31 PM
# Your interview score of 9.30/10 beats 91% of all users.
# Time Spent: 5 minutes 56 seconds
# Time Allotted: 1 hour 30 minutes
#

#
# 1342. Number of Steps to Reduce a Number to Zero
#
# Q1: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# A1: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/504160/Javascript-Python3-C%2B%2B-1-Liners
#
class Solution:
    def numberOfSteps (self, x: int) -> int:
        return 0 if not x else 1 + self.numberOfSteps(x - 1 if x % 2 else x // 2)

#
# 1265. Print Immutable Linked List in Reverse
#
# Q2: https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
# A2: https://leetcode.com/problems/print-immutable-linked-list-in-reverse/discuss/436558/Javascript-Python3-C%2B%2B-1-Liners
#
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
