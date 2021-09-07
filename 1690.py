from typing import List


class Solution: #모범답안
    def stoneGameVII(self, S: List[int]) -> int:
        """

        """
        N, dp = len(S), [0] * len(S)
        for i in range(N - 2, -1, -1):
            total = S[i]
            for j in range(i + 1, N):
                total += S[j]
                dp[j] = max(total - S[i] - dp[j], total - S[j] - dp[j-1])
        return dp[-1]
sol = Solution()
print(sol.stoneGameVII([5,3,1]))