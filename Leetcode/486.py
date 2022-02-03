# 486. Predict the Winner

class Solution(object):
    def PredictTheWinner(self, nums):
        def simulate(remains):
            if not remains: return 0
            if len(remains) == 1: return remains[0]
            return max(remains[0] - simulate(remains[1:]), remains[len(remains)-1] - simulate(remains[:len(remains)-1]))
        return simulate(nums) >= 0

sol = Solution()
print(sol.PredictTheWinner(nums = [1,5,233,7]))
