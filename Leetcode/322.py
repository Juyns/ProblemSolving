# 322. Coin Change

from typing import List
# 이거 완전 다시!!!

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            if dp[i] == -1: dp[i] = getDp(dp[i])
                
        return dp[amount]

sol = Solution()
print(sol.coinChange(coins = [186,419,83,408], amount = 6249))
