#
# 1647. Minimum Deletions to Make Character Frequencies Unique
#
# Q: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# A: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/927497/Kt-Js-Py3-Cpp-Map-%2B-Seen-Counts
#

from collections import Counter

class Solution:
    def minDeletions(self, s: str, dels = 0) -> int:
        m = Counter(s)
        seen = set()
        for _, cnt in m.items():
            while cnt and cnt in seen:
                dels += 1
                cnt -= 1
            seen.add(cnt)
        return dels
