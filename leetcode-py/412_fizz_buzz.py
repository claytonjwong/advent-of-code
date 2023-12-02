#
# 412. Fizz Buzz
#
# Q: https://leetcode.com/problems/fizz-buzz/
# A: https://leetcode.com/problems/fizz-buzz/discuss/812833/Javascript-Python3-C%2B%2B-1-Liners
#

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [] if not n else self.fizzBuzz(n - 1) + (['FizzBuzz'] if not (n % 3) and not (n % 5) else ['Fizz'] if not (n % 3) else ['Buzz'] if not (n % 5) else [f'{n}'])
