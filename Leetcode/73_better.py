# 73번문제 O(1) space complexity

class Solution(object):
    def setZeroes(self, matrix):
        """
            공간복잡도를 1로 만들기 위해 쟁점이었던 것-> 다른 요소를 0이나 1로 바꾸면 헷갈리지 않는가?
            -> 해결책: 위든 아래든 가장 끝 프레임을 잡음. 해당 프레임의 row, column에 내부 matrix의 정보를 저장
            그전에 물론 가장 끝 프레임의 row, column이 0이 되어야 하는지 여부를 저장.
        """
        m, n = len(matrix), len(matrix[0])
        firstRow = firstCol = False
        for i in range(max(m, n)):
            if i < m and matrix[i][0] == 0:
                firstCol = True
            if i < n and matrix[0][i] == 0:
                firstRow = True
            if firstRow and firstCol: break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstCol:
            for i in range(m): matrix[i][0] = 0
        if firstRow:
            for i in range(n): matrix[0][i] = 0
        print(matrix)
        
sol = Solution()
sol.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])