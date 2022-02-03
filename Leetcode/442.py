# 442. Find All Duplicates in an Array

class Solution(object):
    def findDuplicates(self, nums):
        res = []
        dic = {}
        for n in nums:
            if n not in dic: dic[n] = 1
            else: res.append(n)
        return res

sol = Solution()
print(sol.findDuplicates(nums = [1,1,2]))