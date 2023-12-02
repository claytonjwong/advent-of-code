#
# 299. Bulls and Cows
#
# Q: https://leetcode.com/problems/bulls-and-cows/
# A: https://leetcode.com/problems/bulls-and-cows/discuss/402832/Javascript-Python3-C%2B%2B-Map-solutions
#

class Solution:
    def getHint(self, A: str, B: str, bull = 0, cow = 0) -> str:
        A = [int(c) for c in A]
        B = [int(c) for c in B]
        first, second = [0] * 10, [0] * 10
        for i in range(len(A)):
            if A[i] == B[i]:
                bull += 1             # case 1: same digit, increment bull
            else:
                first[A[i]] += 1      # case 2: diff digit, increment corresponding digit count
                second[B[i]] += 1
        for i in range(10):
            cow += min(first[i], second[i])
        return f'{bull}A{cow}B'
