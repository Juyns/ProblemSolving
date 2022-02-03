class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        # difficulty[i], profit[i] - of i th job
        # worker[j] - jth worker only can complete a job that difficulty <= worker[j]
        # 모든 worker에 최대 하나의 job만 배분가능. 하지만 하나의 job은 여러 worker에 배분 가능
        # return maximum profit
        n, m = len(difficulty), len(worker) # num of jobs and workers
        tups = []
        maxVal = 0
        for i in range(n):
            tups.append((difficulty[i], profit[i]))
        tups.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        ind = 1
        dp = [0]
        while tups: # stack
            (dif, pro) = tups[-1]
            if ind >= dif:
                dp.append(max(dp[ind-1], pro))
                if ind == dif:
                    while tups and tups[-1][0] == ind:
                        tups.pop()
            else:
                dp.append(dp[ind-1])
            ind += 1
        res = 0
        for w in worker:
            if w >= len(dp): res += dp[-1]
            else: res += dp[w]
        return res
        
sol = Solution()
print(sol.maxProfitAssignment(difficulty = [49,49,76,88,100], profit = [5,8,75,89,94], worker = [98,72,16,27,76]))        
        


