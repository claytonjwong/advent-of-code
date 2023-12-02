#
# 1512. Number of Good Pairs
#
# Q: https://leetcode.com/problems/number-of-good-pairs/
# A: https://leetcode.com/problems/number-of-good-pairs/discuss/731629/Javascript-and-C%2B%2B-solutions
#

class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        return sum(list(map(lambda row: len(list(filter(lambda pred: pred, row))), [[A[i] == A[j] for j in range(i + 1, len(A))] for i in range(len(A))])))
