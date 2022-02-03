# 73. Set Matrix Zeroes

class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        stack = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: stack.append((i, j))
        while stack:
            a, b = stack.pop()
            for i in range(n):
                matrix[a][i] = 0
            for i in range(m):
                matrix[i][b] = 0
