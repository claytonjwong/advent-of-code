#
# 881. Boats to Save People
#
# Q: https://leetcode.com/problems/boats-to-save-people/
# A: https://leetcode.com/problems/boats-to-save-people/discuss/1014992/Kt-Js-Py3-Cpp-Greedily-Consume-Boats
#

# concise
class Solution:
    def numRescueBoats(self, A: List[int], K: int, cnt = 0) -> int:
        A.sort()
        N = len(A)
        i = 0
        j = N - 1
        while i <= j:
            if i != j and A[i] + A[j] <= K:
                i += 1                       # 🙂 i-th person sometimes fits in the boat ⛵️
            cnt += 1; j -= 1                 # 🙂 j-th person always    fits in the boat ⛵️
        return cnt                           # 🎯 minimum boat count via 💰 greedy consumption

# verbose
class Solution:
    def numRescueBoats(self, A: List[int], K: int, cnt = 0) -> int:
        A.sort()
        N = len(A)
        i = 0
        j = N - 1
        while i <= j:
            if A[i] + A[j] <= K:             # ⛵️ case 1: both 🙂 i-th and 🙂 j-th person
                cnt += 1; i += 1; j -= 1
            else:                            # ⛵️ case 2: only 😕 j-th person
                cnt += 1; j -= 1
        return cnt                           # 🎯 minimum boat count via 💰 greedy consumption
