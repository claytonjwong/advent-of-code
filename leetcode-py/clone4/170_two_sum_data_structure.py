#
# 170. Two Sum III - Data structure design
#
# Q: https://leetcode.com/problems/two-sum-iii-data-structure-design/
# A: https://leetcode.com/problems/two-sum-iii-data-structure-design/discuss/594312/Javascript-Python3-C%2B%2B-Map-Count-of-X
#

class TwoSum:
    def __init__(self):
        self.m = {}

    def add(self, x: int) -> None:
        if x not in self.m:
            self.m[x] = 0
        self.m[x] += 1

    def find(self, x: int) -> bool:
        for y, cnt in self.m.items():
            t = x - y
            if t in self.m:
                if t != y or 1 < cnt:
                    return True
        return False
