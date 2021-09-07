# 240. Search a 2D Matrix II

class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, 0
        rowStart, colStart = 0, 0
        for i in range(m):
            if matrix[i][0] == target: return True
            if matrix[i][0] > target:
                j = 0
                while j < n and row < m and matrix[row][j] < target:
                    colStart = j
                    j += 1
                break
            else: row = i
        for i in range(n):
            if matrix[0][i] == target: return True
            if matrix[0][i] > target:
                j = 0
                while j < m and col < n and matrix[j][col] < target:
                    rowStart = j
                    j += 1
                break
            else: col = i
        for i in range(rowStart, row+1):
            for j in range(colStart, col+1):
                if matrix[i][j] == target: return True
        
        return False
    

sol = Solution()

print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
print(sol.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 19))
print(sol.searchMatrix([[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]], 13))

print(sol.searchMatrix([[-1,3]], 1))
