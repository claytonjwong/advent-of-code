#
# 228. Summary Ranges
#
# Q: https://leetcode.com/problems/summary-ranges/
# A: https://leetcode.com/problems/summary-ranges/discuss/913748/Kt-Js-Py3-Cpp-Monotonic-Chains
#

from typing import List

class Solution:
    def summaryRanges(self, A: List[int]) -> List[str]:
        chain = []
        chains = []
        def save():
            nonlocal chain, chains
            chains.append(str(chain[0]) if chain[0] == chain[-1] else f'{chain[0]}->{chain[-1]}')
            chain = []
        for x in A:
            if len(chain) and x != 1 + chain[-1]:  # 🚫 broken link in the chain 🔗
                save()
            chain.append(x)
        if len(chain):
            save()
        return chains
