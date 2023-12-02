#
# 905. Sort Array By Parity
#
# Q: https://leetcode.com/problems/sort-array-by-parity/
# A: https://leetcode.com/problems/sort-array-by-parity/discuss/172134/Javascript-Python3-C%2B%2B-1-Liners
#

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return list(filter(lambda x: not (x & 1), A)) + list(filter(lambda x: x & 1, A))
