#
# 1103. Distribute Candies to People
#
# Q: https://leetcode.com/problems/distribute-candies-to-people/
# A: https://leetcode.com/problems/distribute-candies-to-people/discuss/323409/Javascript-Python3-C%2B%2B-Brute-Force
#

from typing import List

class Solution:
    def distributeCandies(self, k: int, N: int, candy = 1) -> List[int]:
        ans = [0] * N
        while k:
            for i in range(N):
                take = min(candy, k)  # ⭐️ take candy (not exceeding available k candies)
                ans[i] += take
                k -= take
                candy += 1
        return ans
