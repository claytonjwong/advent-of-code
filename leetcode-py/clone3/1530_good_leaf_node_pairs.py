#
# 1530. Number of Good Leaf Nodes Pairs
#
# Q: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
# A: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/758931/Javascript-Python3-C%2B%2B-post-order-Map-distance-count
#

class Solution:
    def countPairs(self, root: TreeNode, T: int) -> int:
        cnt = 0
        def go(root):
            nonlocal cnt
            m = collections.Counter()
            if not root:
                return m
            L = go(root.left)
            R = go(root.right)
            if not root.left and not root.right:
                m[1] = 1 # ⭐️ add leaf node to map with distance 1 and count 1
            for dist1, cnt1 in L.items():
                for dist2, cnt2 in R.items():
                    if dist1 + dist2 <= T: # 🎯 count "good" leaf node pairs
                        cnt += cnt1 * cnt2
            # 📌 propagate coalesced child node maps up the recursive stack (dist + 1 because parent is dist + 1 from child)
            for [dist1, cnt1] in L.items(): m[dist1 + 1] += cnt1
            for [dist2, cnt2] in R.items(): m[dist2 + 1] += cnt2
            return m
        go(root)
        return cnt
