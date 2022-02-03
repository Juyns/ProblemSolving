# 684. Redundant Connection

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        lastAnswer = []

        def find(x):
            if parent[x] == x: return x
            else:
                temp = find(parent[x])
                parent[x] = temp
                return temp
        def union(x, y):
            a, b = find(x), find(y)
            parent[max(a, b)] = min(a, b)
            parent[x] = min(a, b)
            parent[y] = min(a, b)

        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]

            
            if find(a) == find(b): lastAnswer = [a, b]
            union(a, b)
        return lastAnswer
    
sol = Solution()
print(sol.findRedundantConnection(edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]))