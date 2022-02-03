import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):        
        graph, path, search = {}, [], []
        for _ in range(n):
            path.append(0)
        path[start] = 1
        for i in range(len(edges)):
            a, b = edges[i]
            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        heapq.heappush(search, (start, -1))
        
        while search:
            node, prob = heapq.heappop(search)
            prob *= -1
            if node not in graph: continue 
            for nextNode, nextProb in graph[node]:
                newProb = prob*nextProb
                if newProb > path[nextNode]:
                    path[nextNode] = newProb
                    heapq.heappush(search, (nextNode, -newProb))
        
        return path[end]

sol = Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))