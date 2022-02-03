# 1503. Last Moment Before All Ants Fall Out of a Plank

class Solution(object):
    def getLastMoment(self, n, left, right):
        return max(max(left or [0]), n - min(right or [n]))

sol = Solution()
print(sol.getLastMoment(n = 4, left = [0,4,3,5,8,9], right = [0,1]))
        
