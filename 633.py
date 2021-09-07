import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while (l <= r):
            current = l**2 + r**2
            if current == c: return True
            elif current < c: l += 1
            else: r -= 1
        return False

sol = Solution()
print(sol.judgeSquareSum(c = 1000))