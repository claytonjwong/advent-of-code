#
# 1460. Make Two Arrays Equal by Reversing Sub-arrays
#
# Q: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# A: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/discuss/660539/Javascript-and-C%2B%2B-solutions
#

# count frequency
class Solution:
    def canBeEqual(self, A: List[int], B: List[int]) -> bool:
        m = Counter()
        for x in A: m[x] += 1
        for x in B: m[x] -= 1
        return not len(list(filter(lambda pair: pair[1], m.items())))

# sort + compare
class Solution:
    def canBeEqual(self, A: List[int], B: List[int]) -> bool:
        return sorted(A) == sorted(B)
