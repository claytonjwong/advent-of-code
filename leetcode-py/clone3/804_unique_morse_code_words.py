#
# 804. Unique Morse Code Words
#
# Q: https://leetcode.com/problems/unique-morse-code-words/
# A: https://leetcode.com/problems/unique-morse-code-words/discuss/120682/Kt-Js-Py3-Cpp-Seen
#

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, A: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in A:
            encoded = []
            for c in word:
                encoded.append(m[ord(c) - ord('a')])
            seen.add(''.join(encoded))
        return len(seen)
