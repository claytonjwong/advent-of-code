#
# 1524. Number of Sub-arrays With Odd Sum
#
# Q: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# A: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/discuss/754751/Javascript-Python3-C%2B%2B-count-of-evenodd-sums
#
class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        sum = 0
        cnt = [1, 0]
        for i in range(len(A)):
            sum += A[i]
            cnt[sum % 2] += 1
        return (cnt[0] * cnt[1]) % int(1e9 + 7)
