# 909. Snakes and Ladders

from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        direction = {}
        visited = []
        n = len(board[0])
        ind = 1
        toggle = True
        for i in range(n-1, -1, -1):
            if toggle:
                for j in range(n):
                    direction[ind] = board[i][j]
                    ind += 1
                    visited.append(False)
                toggle = False
            else:
                for j in range(n-1, -1 ,-1):
                    direction[ind] = board[i][j]
                    ind += 1
                    visited.append(False)
                toggle = True

        dq = deque()
        dq.append((1, 0))
        while dq:
            comp, level = dq.popleft()
            if comp == n**2: return level
            for num in range(comp + 1, min(comp + 6, n**2)+1):
                if direction[num] != -1:
                    if not visited[direction[num]-1]:
                        visited[direction[num]-1] = True
                        dq.append((direction[num], level+1))
                else:
                    if not visited[num-1]:
                        visited[num-1] = True
                        dq.append((num, level+1))

        return -1

sol = Solution()
print(sol.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders(board = [[-1,-1],[-1,3]]))