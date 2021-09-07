# 954. Array of Doubled Pairs

from typing import List 
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(sorted(arr, key=lambda x: abs(x)))
        for i in count.keys():
            if count[i] == 0:
                continue
            count[i*2] -= count[i]
            if count[i*2] < 0:
                return False
        return True

sol = Solution()
print(sol.canReorderDoubled(arr = [4,-2,2,-4,0,0, -1]))