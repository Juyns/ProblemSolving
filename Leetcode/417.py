#417. Pacific Atlantic Water Flow


class Solution(object):
    def pacificAtlantic(self, heights):
        pacific, atlantic = [], []
        seq = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        result = []
        n = len(heights)
        m = len(heights[0])
        for i in range(n):
            pacific.append([])
            atlantic.append([])
            for _ in range(m):
                pacific[i].append(False)
                atlantic[i].append(False)
        
        def dfs(i, j, isDone):
            isDone[i][j] = True
            for a, b in seq:
                x, y = i + a, j + b
                if x < 0 or y < 0 or x > n-1 or y > m-1 or isDone[x][y] or heights[x][y] < heights[i][j]:
                    continue
                dfs(x, y, isDone)
        
        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m-1, atlantic)
            
        for j in range(m):
            dfs(0, j, pacific)
            dfs(n-1, j, atlantic)
            
        
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]: result.append([i, j])
        
        return result


sol = Solution()
print(sol.pacificAtlantic([[1,1],[1,1],[1,1]]))
            
        
                
        
        