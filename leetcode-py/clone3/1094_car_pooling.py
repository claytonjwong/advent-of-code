#
# 1094. Car Pooling
#
# Q: https://leetcode.com/problems/car-pooling/
# A: https://leetcode.com/problems/car-pooling/discuss/857714/Javascript-Python3-C%2B%2B-Map-solutions
#

class Solution:
    def carPooling(self, A: List[List[int]], K: int, total = 0) -> bool:
        m = {}
        for n, i, j in A:
            m[i] =  n if i not in m else m[i] + n
            m[j] = -n if j not in m else m[j] - n
        for _, n in sorted([[i, n] for i, n in m.items()]):
            total += n
            if K < total:
                return False
        return True
