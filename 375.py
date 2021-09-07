# 375. Guess Number Higher or Lower II

class Solution(object):
    def getMoneyAmount(self, n):
        def search(remain):
            l = len(remain)
            if l <= 1: return 0
            if l in memo:
                return remain[memo[l]] + max(search(remain[:memo[l]]), search(remain[memo[l]+1:]))
            else:
                min = maxVal
                minInd = 0
                for i in range(len(remain)):
                    temp = remain[i] + max(search(remain[:i]), search(remain[i+1:]))
                    if temp < min:
                        min = temp
                        minInd = i
                memo[l] = minInd
                return min
        nums = list(range(1, n+1))
        maxVal = 201*100
        memo = {2: 0, 3: 1, 4: 0}
        return search(nums)

sol = Solution()
print(sol.getMoneyAmount(8))
