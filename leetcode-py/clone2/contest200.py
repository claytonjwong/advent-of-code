from typing import List
import collections

#
# 1535. Find the Winner of an Array Game
#
# Q: https://leetcode.com/problems/find-the-winner-of-an-array-game/
# A: https://leetcode.com/problems/find-the-winner-of-an-array-game/discuss/768447/Javascript-Python3-C%2B%2B-Deque-a-b-...-first-two-elements
#

class Solution:
    def getWinner(self, A: List[int], K: int, same = 0) -> int:
        N = len(A)
        if N == 1 or K == 1:         # 💎 edge cases
            return max(A[0], A[1])
        if N <= K:                   # 💎 edge cases
            return max(A)
        q = collections.deque(A)
        while True:                  # compare first two elements: A[ ✅ a, 🚫 b, ... ] 👀
            a = q.popleft()
            b = q.popleft()
            if a < b:                # case 1: ⭐️ diff winner 🚫 b, reset same to 1
                same = 1
            if b < a:                # case 2: ⭐️ same winner ✅ a, increment same by 1
                same += 1
                if same >= K:        #         🎯 same winner ✅ a, target K times
                    return a
            q.appendleft(max(a, b))  # push max to front 👈
            q.append(min(a, b))      # push min to back  👉
