# 826 모범답안

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit)) # zip이용 - 불필요한 코드 줄임
        res = i = best = 0
        for ability in sorted(worker): # 굳이 stack사용할 필요 없음
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res
        
sol = Solution()
print(sol.maxProfitAssignment(difficulty = [49,49,76,88,100], profit = [5,8,75,89,94], worker = [98,72,16,27,76]))        
        


