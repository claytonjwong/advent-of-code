#
# 394. Decode String
#
# Q: https://leetcode.com/problems/decode-string/
# A: https://leetcode.com/problems/decode-string/discuss/941684/Kt-Js-Py3-Cpp-Stack
#

class Solution:
    def decodeString(self, encoded: str, freq = '', word = '') -> str:
        s = []
        for c in encoded:
            if c == '[':
                s.append(word); s.append(freq)
                freq, word = '', ''
            if c == ']':
                last_freq, last_word = s.pop(), s.pop()
                word = last_word + (int(last_freq) * word)
            if c.isdigit(): freq += c
            if c.isalpha(): word += c
        return word
