# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if (not nums): return 0
        if (len(nums) == 1): return 1
        left, right = 0, 1
        maxVal, minVal, maxLen = nums[0], nums[0], 0
        

        while (left <= right and right < len(nums)):
            minVal = min(minVal, nums[right])
            maxVal = max(maxVal, nums[right])

            if maxVal - minVal > limit: #have to renew
                if minVal == nums[left]:
                    minVal = min(nums[left+1:right+1])
                if maxVal == nums[left]:
                    maxVal = max(nums[left + 1:right + 1])
                left += 1
            else:
                maxLen = max(maxLen, right-left+1)
            right += 1
        return maxLen


sol = Solution()
print(sol.longestSubarray(nums = [8,2,4,7], limit = 4))
print(sol.longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
print(sol.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))