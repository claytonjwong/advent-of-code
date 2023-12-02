#
# 1720. Decode XORed Array
#
# Q: https://leetcode.com/problems/decode-xored-array/
# A: https://leetcode.com/problems/decode-xored-array/discuss/1009766/Kt-Js-Py3-Cpp-XOR-Last
#

class Solution:
    def decode(self, A: List[int], K: int) -> List[int]:
        ans = [ K ]
        for x in A:
            ans.append(x ^ ans[-1])
        return ans
