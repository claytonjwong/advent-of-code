#
# 421. Maximum XOR of Two Numbers in an Array
#
# Q: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# A: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/849679/Javascript-Python3-C%2B%2B-Trie-%2B-Greedy-Alternative-Path
#

from typing import List

class Solution:
    def findMaximumXOR(self, A: List[int], best = 0) -> int:
        root = {}                                      # 🌲 trie
        for x in A:
            xor = 0
            cur = root                                 # 👀 current path in trie for inserting binary representation of x
            alt = root                                 # 🤔 alternative path for pre-existing values in trie
            for i in range(31, -1, -1):
                p = 1 if 0 < (x & (1 << i)) else 0     # 🚙 direction p and opposite 🚗 direction q
                q = p ^ 1
                cur[p] = cur[p] if p in cur else {}    # 🚙 add direction p to 👀 current path (as needed)
                cur = cur[p]
                if q in alt:                           # 🚗 diff direction q for 🤔 alternative path (💰 greedily take this path whenever possible)
                    alt = alt[q]; xor ^= (1 << i)
                else:                                  # 🚙 same direction p for 🤔 alternative path
                    alt = alt[p]
            best = max(best, xor)                      # 🎯 max xor
        return best
