#
# 1603. Design Parking System
#
# Q: https://leetcode.com/problems/design-parking-system/
# A: https://leetcode.com/problems/design-parking-system/discuss/876790/Javascript-Python3-C%2B%2B-Concise-solutions
#

class ParkingSystem:
    def __init__(self, a: int, b: int, c: int):
        self.A = [0, a, b, c]
    def addCar(self, x: int) -> bool:
        if not self.A[x]:
            return False
        self.A[x] -= 1
        return True
