#
# 884. Uncommon Words from Two Sentences
#
# Q: https://leetcode.com/problems/uncommon-words-from-two-sentences/
# A: https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/159907/Javascript-Python3-C%2B%2B-Word-Counter
#

from typing import List

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = split(' ', A) + split(' ', B)
        m = collections.Counter(words)
        return list(filter(lambda word: m[word] == 1, words))
