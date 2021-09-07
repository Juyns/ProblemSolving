#16. 3Sum Closest

from typing import List
from itertools import combinations

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def getCalculate(current):
            return abs(max(current, target) - min(current, target))
        com = list(combinations(nums, 3))
        res = 0, float('inf')
        for a, b, c in com:
            temp = a + b + c, getCalculate(a + b + c)
            if temp[1] == 0: return temp[0]
            if res[1] > temp[1]: res = temp
        return res[0]

sol = Solution()
print(sol.threeSumClosest(nums = [1,1,-1,-1,3], target = 3))