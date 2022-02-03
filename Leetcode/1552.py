# 1552. Magnetic Force Between Two Balls

import math

class Solution(object):
    def maxDistance(self, position, m):
        def find(l, offset):
            i = 1
            ans = [l]
            while ans[-1]+i <= len(position)-1:
                if position[ans[-1]+i] - position[ans[-1]] >= offset:
                    ans.append(ans[-1]+i)
                    i = 1
                else: i += 1
                if len(ans) == m: return True
            return False
        position.sort()
        startPoint = position[0]
        endPoint = position[-1]
        offset = int(math.ceil((endPoint-startPoint)/(m-1)))

        init = 0
        while offset > 0:
            if len(position) - init +1 < m:
                offset -= 1
                init = 0
                continue 
            if find(init, offset): return offset
            else: init += 1
        return -1



sol = Solution()

print(sol.maxDistance(position =[79,74,57,22], m = 4))
       