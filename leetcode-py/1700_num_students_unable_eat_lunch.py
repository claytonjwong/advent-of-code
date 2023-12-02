#
# 1700. Number of Students Unable to Eat Lunch
#
# Q: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# A: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/discuss/987305/Kt-Js-Py3-Cpp-Do-we-HAVE-what-we-NEED
#

from typing import List

class Solution:
    def countStudents(self, need: List[int], have: List[int]) -> int:
        m = Counter(need)
        need = deque(need)
        have = deque(have)
        while len(have) and have[0] in m and 0 < m[have[0]]:
            if need[0] != have[0]:
                need.append(need.popleft())
                continue
            m[have[0]] -= 1
            need.popleft()
            have.popleft()
        return len(need)
