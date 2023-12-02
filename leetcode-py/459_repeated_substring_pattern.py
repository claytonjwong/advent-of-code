#
# 459. Repeated Substring Pattern
#
# Q: https://leetcode.com/problems/repeated-substring-pattern/
# A: https://leetcode.com/problems/repeated-substring-pattern/discuss/826659/Javascript-Python3-C%2B%2B-Recursive-%2B-.-Iterative
#

# recursive
class Solution:
    def repeatedSubstringPattern(self, S: str, k = float('inf')) -> bool:
        k = k if k != float('inf') else len(S) // 2
        return False if not k else (not (len(S) % k) and all([len(S) <= i + k or S[i] == S[i + k] for i in range(len(S) - k)])) or self.repeatedSubstringPattern(S, k - 1)

# iterative
class Solution:
    def repeatedSubstringPattern(self, S: str) -> bool:
        N = len(S)
        for k in range(1, (N // 2) + 1):
            if N % k:
                continue                            # 🚫 candidate pattern of length k must evenly divide N
            i = 0
            while i + k < N and S[i] == S[i + k]:   # 🔍 explore candidate pattern of length k
                i += 1
            if i + k == N:
                return True                         # 🎯 match found for candidate pattern of length k
        return False
