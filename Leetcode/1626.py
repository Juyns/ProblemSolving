# 1626. Best Team With No Conflicts

class Solution(object):
    def bestTeamScore(self, scores, ages):
        players = sorted(list(zip(ages, scores)), key=lambda x: (x[0], x[1]))
        dp = [0 for _ in range(len(players))]
        dp[0] = players[0][1]
        maxVal = dp[0]
        for i in range(1, len(players)):
            dp[i] = players[i][1]
            for j in range(i-1, -1, -1):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j]+players[i][1])
            maxVal = max(maxVal, dp[i])
        return maxVal

sol = Solution()
print(sol.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
