#
# 140. Word Break II
#
# Q: https://leetcode.com/problems/word-break-ii/
# A: https://leetcode.com/problems/word-break-ii/discuss/765548/Javascript-Python3-C%2B%2B-top-down-%2B-bottom-up-(partial)
#

from typing import List

# naive DFS + BT results in TLE which cannot be memoized,
# since there is no return value to coalesce/memoize
class Solution:
    def wordBreak(self, S: str, A: List[str]) -> List[str]:
        words = []
        N = len(S)
        dict = set(A)
        def go(i = 0, path = []):
            print(i, path)
            if i == N:
                words.append(path.copy())
                return
            for j in range(i + 1, N + 1): # ⭐️ candidate substrings S[i..j), ie. from i inclusive to j non-inclusive
                cand = S[i:j]
                if cand in dict:
                    path.append(cand)
                    go(j, path)           # 🚀 DFS + BT
                    path.pop()
        go()
        return list(map(lambda row: ' '.join(row), words))

# brute-force
class Solution:
    def wordBreak(self, S: str, A: List[str]) -> List[str]:
        N = len(S)
        dict = set(A)
        def go(i = 0):
            words = []
            if i == N:                              # 🛑 base case: "empty" word can be constructed when there are no remaining characters in S
                return [[]]
            for j in range(i + 1, N + 1):           # ⭐️ candidate substrings S[i..j), ie. from i inclusive to j non-inclusive
                cand = S[i:j]
                if cand in dict:
                    for tail in go(j):
                        words.append([cand] + tail) # 🚀 DFS concat tails onto 🔍 found candidates, ie. build 🎯 words from 👈 right-to-left
            return words
        return list(map(lambda row: ' '.join(row), go()))

# memo
class Solution:
    def wordBreak(self, S: str, A: List[str]) -> List[str]:
        N = len(S)
        m = [None] * (N + 1)
        dict = set(A)
        def go(i = 0):
            if m[i] != None:                        # 🤔 memo
                return m[i]
            words = []
            if i == N:                              # 🛑 base case: "empty" word can be constructed when there are no remaining characters in S
                return [[]]
            for j in range(i + 1, N + 1):           # ⭐️ candidate substrings S[i..j), ie. from i inclusive to j non-inclusive
                cand = S[i:j]
                if cand in dict:
                    for tail in go(j):
                        words.append([cand] + tail) # 🚀 DFS concat tails onto 🔍 found candidates, ie. build 🎯 words from 👈 right-to-left
            m[i] = words
            return m[i]
        return list(map(lambda row: ' '.join(row), go()))

# bottom up
class Solution:
    def wordBreak(self, S: str, A: List[str]) -> List[str]:
        N = len(S)
        dp = list(map(lambda _: [], [None] * (N + 1)))         # 🤔 memo
        dp[N] = [[]]                                           # 🛑 base case: "empty" word can be constructed when there are no remaining characters in S
        dict = set(A)
        for i in range(N - 1, -1, -1):                         # ⭐️ candidate substrings S[i..j), ie. from i inclusive to j non-inclusive
            for j in range(i + 1, N + 1):
                cand = S[i:j]
                if cand in dict:
                    for tail in dp[j]:
                        dp[i].append([cand] + tail)            # 🚀 DFS concat tails onto 🔍 found candidates, ie. build 🎯 words from 👈 right-to-left
        return list(map(lambda words: ' '.join(words), dp[0]))
