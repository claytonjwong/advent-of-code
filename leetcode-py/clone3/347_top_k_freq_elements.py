#
# 347. Top K Frequent Elements
#
# Q: https://leetcode.com/problems/top-k-frequent-elements/
# A: https://leetcode.com/problems/top-k-frequent-elements/discuss/740792/Javascript-Python3-C%2B%2B
#

class Solution:
    def topKFrequent(self, A: List[int], K: int, m = {}) -> List[int]:
        return [x for x, _ in Counter(A).most_common(K)]
