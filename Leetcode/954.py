# 954. Array of Doubled Pairs

from typing import List 

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        instances = {}
        zeroCount = 0
        
        for i in range(len(arr)):
            if arr[i] == 0:
                zeroCount += 1
                continue
            if arr[i] not in instances:
                instances[arr[i]] = 0
            instances[arr[i]] += 1
        if zeroCount % 2 != 0: return False
        arr = sorted(arr, key=lambda x: abs(x))
        for i in arr:
            if i not in instances: continue
            if instances[i] == 0: continue
            if i*2 in instances:
                if instances[i*2] >= instances[i]:
                    instances[i*2] -= instances[i]
                    instances[i] = 0
                else: return False
            else:
                return False
        return True


sol = Solution()
print(sol.canReorderDoubled(arr = [0,0]))
print(sol.canReorderDoubled(arr = [-1,4,6,8,-4,6,-6,3,-2,3,-3,-8]))

"""
    def mutantMerge(self, arr):
        if not arr: return []

        if len(arr) == 1:
            if arr[0] == 0: return []
            elif arr[0] < 0: return [-1*arr[0]]
            else: return arr
        midIndex = len(arr)//2
        low = self.mutantMerge(arr[:midIndex])
        high = self.mutantMerge(arr[midIndex:])
        merged = []
        l, h = 0, 0
        while l < len(low) and h < len(high):
            if low[l] < high[h]:
                merged.append(low[l])
                l+=1
            else:
                merged.append(high[h])
                h += 1
        merged += low[l:]
        merged += high[h:]
        return merged
"""