#
# 1286. Iterator for Combination
#
# Q: https://leetcode.com/problems/iterator-for-combination/
# A: https://leetcode.com/problems/iterator-for-combination/discuss/789522/Javascript-Python3-C%2B%2B-Recursive-DFS-%2B-BT
#

class CombinationIterator:
    def __init__(self, A: str, K: int):
        self.A = A
        self.K = K
        self.i = 0
        self.combos = []
        self.go()

    def go(self, i = 0, path = []) -> None:
        A, K = self.A, self.K
        if len(path) == K:
            self.combos.append(path.copy())
            return
        if i == len(A):
            return
        self.go(i + 1, path + [A[i]])  # ✅ with A[i]
        self.go(i + 1, path)           # 🚫 withtout A[i]

    def next(self) -> str:
        res = self.combos[self.i]
        self.i += 1
        return ''.join(res)

    def hasNext(self) -> bool:
        return self.i < len(self.combos)
