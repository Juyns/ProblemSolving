# 1706. Where Will the Ball Fall

class Solution(object):
    def findBall(self, grid):
        def pathFind(current, level):
            if current == 0:
                if grid[level][0] == -1: return -1
                else:
                    if grid[level][1] == 1: return current+1
                    else: return -1
            elif current == len(grid[level])-1:
                if grid[level][-1] == 1: return -1
                else:
                    if grid[level][-2] == -1: return current-1
                    else: return -1
            else:
                l = grid[level][current]
                r = grid[level][current+l]
                if l * r < 0: return [-1]
                else: return current+l

        balls = [i for i in range(len(grid[0]))]
        if len(balls) == 1: return -1
        for i in range(len(grid)):
            for j in range(len(balls)):
                if balls[j] != -1: balls[j] = pathFind(balls[j], i)
        return balls

sol = Solution()
print(sol.findBall(grid = [[-1]]))
  
