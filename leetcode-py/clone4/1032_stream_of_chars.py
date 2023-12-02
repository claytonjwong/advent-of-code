#
# 1032. Stream of Characters
#
# Q: https://leetcode.com/problems/stream-of-characters/
# A: https://leetcode.com/problems/stream-of-characters/discuss/807725/Javascript-Python3-C%2B%2B-Trie-solutions
#

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class StreamChecker:
    def __init__(self, A: List[str]):
        self.A = A
        self.root = TrieNode()
        self.cand = []
        for word in A:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True
    def query(self, c: str) -> bool:
        self.cand[:] = [node for node in self.cand if c in node.children]  # 🚫 remove candidate nodes which do not have child c
        for i in range(len(self.cand)):
            self.cand[i] = self.cand[i].children[c]
        if c in self.root.children:
            self.cand.append(self.root.children[c])
        return any(node.isEnd for node in self.cand)
