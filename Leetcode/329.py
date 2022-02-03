# 329. Longest Increasing Path in a Matrix

class Solution(object):
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        done = [[False for _ in range(n)] for _ in range(m)]
        direction = [(0,1), (1,0), (0, -1), (-1, 0)]
        info = {}
        def dfs(i, j):
            if (i, j) in info: return info[(i, j)]
            cand = []
            for a, b in direction:
                x, y = i+a, j+b
                if x < 0 or y < 0 or x > m-1 or y > n-1 or done[x][y] or matrix[x][y] <= matrix[i][j]:
                    continue
                done[x][y] = True
                cand.append(1 + dfs(x, y))
                done[x][y] = False
            if not cand: return 1
            else:
                info[(i, j)] = max(cand)
                return max(cand)

        for i in range(m):
            for j in range(n): 
                if not done[i][j]:
                    done[i][j] = True
                    dfs(i, j)
                    done[i][j] = False

        return max(info.values()) if info.values() else 1



sol = Solution()
print(sol.longestIncreasingPath([[3,4,5],[1,7,6],[1,8,9]]))
