#
# 260. Single Number III
#
# Q: https://leetcode.com/problems/single-number-iii/
# A: https://leetcode.com/problems/single-number-iii/discuss/750939/Javascript-Python3-C%2B%2B-Seen-and-Counter-solutions-O(N)-memory
#

# seen set
class Solution:
    def singleNumber(self, A: List[int]) -> List[int]:
        seen = set()
        for x in A:
            seen.remove(x) if x in seen else seen.add(x) # 🚫 remove x seen twice 👀 and ✅ keep x seen once 👀
        return seen

# counter
class Solution:
    def singleNumber(self, A: List[int]) -> List[int]:
        m = Counter()
        for x in A:
            m[x] += 1
        return list(map(lambda pair: pair[0], filter(lambda pair: pair[1] == 1, m.items())))
