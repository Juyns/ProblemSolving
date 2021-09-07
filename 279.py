# 279. Perfect Squares

import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n+1):
            dp.append(n+1)
            for j in range(1, int(math.sqrt(i))+1):
                if j**2 <= i:
                    dp[i] = min(dp[i], dp[i-j**2]+1)
                else: break
        return dp[n]

sol = Solution()
print(sol.numSquares(12))

