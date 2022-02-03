# 1834. Single-Threaded CPU

import heapq

class Solution(object):
    def getOrder(self, tasks):
        timeHeap, valHeap, result =  [], [], []
        def hPush(time):
            if timeHeap and time < timeHeap[0][0]: #작업을 더 넣을 수 없는경우
                if valHeap: return time
                else: time = timeHeap[0][0]
            while timeHeap and timeHeap[0][0] <= time:
                comp = heapq.heappop(timeHeap)
                heapq.heappush(valHeap, (comp[1][2], comp[1][0]))
            return time

        for comp in enumerate(tasks):
            heapComp = comp[0], comp[1][0], comp[1][1] #ind, time, val
            heapq.heappush(timeHeap, (heapComp[1], heapComp))

        lastTime = timeHeap[0][0]
        hPush(timeHeap[0][0])

        while valHeap:
            v, i = heapq.heappop(valHeap)
            result.append(i)
            lastTime = hPush(lastTime+v)

        return result

sol = Solution()
print(sol.getOrder(tasks = [[46,9],[46,42],[30,46],[30,13],[30,24],[30,5],[30,21],[29,46],[29,41],[29,18],[29,16],[29,17],[29,5],[22,15],[22,13],[22,25],[22,49],[22,44]]))
        