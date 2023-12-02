#
# 212. Word Search II
#
# Q: https://leetcode.com/problems/word-search-ii/
# A: https://leetcode.com/problems/word-search-ii/discuss/713117/Javascript-and-C%2B%2B-solutions
#

from typing import List

class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        found = set()
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isEnd = False
        root = TrieNode()
        def add(word):
            cur = root
            for c in word:
                if not c in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True
        for word in words:
            add(word)
        M = len(A)
        N = len(A[0]) if M else 0
        def go(i, j, cur, path = [], seen = set()):
            nonlocal found
            if f'{i},{j}' in seen: # ❌ already seen i,j 👀
                return
            if cur.isEnd: # 🎯 found word
                found.add(''.join(path))
            seen.add(f'{i},{j}')    # 👀 ✅ seen forward-tracking
            for u, v in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]: # clockwise [ 👆, 👉, 👇, 👈 ]
                if not (u < 0 or u == M or v < 0 or v == N) and A[u][v] in cur.children:
                    path.append(A[u][v]) # 🚌 ✅ path forward-tracking
                    go(u, v, cur.children[A[u][v]], path, seen)
                    path.pop()           # 🚌 🚫 path back-tracking
            seen.remove(f'{i},{j}') # 👀 🚫 seen back-tracking
        for i in range(M):
            for j in range(N):
                if A[i][j] in root.children:
                    go(i, j, root.children[A[i][j]], [A[i][j]])
        return found
