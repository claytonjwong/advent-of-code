#
# 1496. Path Crossing
#
# Q: https://leetcode.com/problems/path-crossing/
# A: https://leetcode.com/problems/path-crossing/discuss/709194/Javascript-and-C%2B%2B-solutions
#
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        i, j = 0, 0
        seen = set([ f'{i},{j}' ])
        for dir in path:
            if dir == 'N': i -= 1 # -1 for 👆 North or 👈 West
            if dir == 'W': j -= 1
            if dir == 'S': i += 1 # +1 for 👇 South or 👉 East
            if dir == 'E': j += 1
            if f'{i},{j}' in seen: # 🚫 path seen 👀
                return True
            seen.add(f'{i},{j}')
        return False               # ✅ path *not* seen 👀
