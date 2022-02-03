from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[]
        courseDic = {}
        result=True
        
        def check(ind, tempv):
            visited[ind]=True
            current=True

            for comp in courseDic[ind]:
                if tempv[comp]: return False #circulation found
                else:
                    tempv[comp]=True 
                    current= check(comp, tempv)
                    tempv[comp]=False
                if not current: break
            return current


        
        for i in range(numCourses):
            visited.append(False)
            courseDic[i] = []
        for crs, precrs in prerequisites:
            if crs==precrs: return False
            courseDic[precrs].append(crs)
            
        for i in courseDic.keys():
            if not visited[i]:
                tempVisited=[]
                for i in range(numCourses):
                    tempVisited.append(False)
                visited[i]=True
                result=check(i, tempVisited)
            if not result: break
        return result