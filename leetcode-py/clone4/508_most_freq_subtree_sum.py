#
# 508. Most Frequent Subtree Sum
#
# Q: https://leetcode.com/problems/most-frequent-subtree-sum/
# A: https://leetcode.com/problems/most-frequent-subtree-sum/discuss/780522/Javascript-Python3-C%2B%2B-solutions
#

from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode, best = 0) -> List[int]:
        if not root:
            return []
        m = {}
        def go(root):
            nonlocal best
            L = go(root.left)  if root.left  else 0
            R = go(root.right) if root.right else 0
            sum = root.val + L + R
            if not sum in m:
                m[sum] = 0
            m[sum] += 1
            best = max(best, m[sum])
            return sum
        go(root)
        return list(map(lambda pair: pair[0], filter(lambda pair: pair[1] == best, m.items())))
