#
# 1520. Maximum Number of Non-Overlapping Substrings
#
# Q: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
# A: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/discuss/749421/Javascript-Python3-C%2B%2B-beginend-index-%2B-greedy-consumption
#

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ans = []
        # 1. track the begin index and end index of each character
        beg = { c: s.index(c)  for c in set(s) }
        end = { c: s.rindex(c) for c in set(s) }
        # 2. update the min begin index and max end index for each unique character candidate
        seen = set()
        for cand in s:
            if cand in seen:
                continue
            seen.add(cand)
            i, j = beg[cand], end[cand]
            mini, maxj = i, j
            while i <= maxj:
                c = s[i]
                mini = min(mini, beg[c])
                maxj = max(maxj, end[c])
                i += 1
            beg[cand], end[cand] = mini, maxj
        # 3. sort the intervals by end index for greedy consumption of non-overlapping intervals
        A = sorted(seen, key = lambda c: end[c])
        pre = -1 # end index inclusive of previous interval
        for cand in A:
            i = beg[cand]
            j = end[cand]
            if pre < i: # non-overlapping interval
                ans.append(s[i : j + 1]) # 🎯 +1 for i..j inclusive
                pre = j
        return ans
