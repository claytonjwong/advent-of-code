#
# 1415. The k-th Lexicographical String of All Happy Strings of Length n
#
# Q: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# A: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/589380/Javascript-and-C%2B%2B-solutions
#

class Solution:
    def getHappyString(self, N: int, K: int, ans = '') -> str:
        def go(i = 0, path = []):
            nonlocal ans, K
            if not K:
                return
            if i == N:
                K -= 1
                if not K:
                    ans = ''.join(path) # 🎯 K-th happy string
                return
            for c in ['a', 'b', 'c']:
                if not len(path) or c != path[-1]:
                    path.append(c)  # 👀 ✅ path forward-tracking
                    go(i + 1, path) # 🚀 DFS explore path
                    path.pop()      # 👀 🚫 path back-tracking
        go()
        return ans
