# 1536. Minimum Swaps to Arrange a Binary Grid

class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)
        totalSwap = 0
        def find(start):
            for i in range(start, n):
                if sum(grid[i][start+1:]) == 0: return i
            return -1
        def swap(top, bottom):
            swapCount = 0
            if top == bottom: return 0
            for i in range(bottom, top, -1):
                temp = grid[i]
                grid[i] = grid[i-1]
                grid[i-1] = temp
                swapCount += 1
            return swapCount
        for i in range(n):
            found = find(i)
            if found == -1: return -1
            totalSwap += swap(i, found)
        return totalSwap
            



sol = Solution()
print(sol.minSwaps(grid =[[1,0,0],[1,1,0],[1,1,1]]))
