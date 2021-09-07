# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def check(startPoint, endPoint):
            mini = startPoint
            maxi = startPoint
            result = True
            for i in range(startPoint, endPoint+1):
                if nums[mini] > nums[i]:
                    mini = i
                if nums[maxi] < nums[i]:
                    maxi = i
                if nums[maxi]-nums[mini] > limit:
                    result = False
                    break
            return result, mini, maxi
        
        minInd, maxInd = 0, 0
        maxLen = 0
        current = deque()
        for i in range(len(nums)): #최대 - 1까지
            current.append(i)
            if nums[minInd] > nums[i]:
                if nums[maxInd] - nums[i] <= limit: #배열이 계속될 수 있을 때
                    minInd = i
                else: #이전 요소를 버려가며 갱신해야 할 때
                    passOk = False
                    #변경 전, 지금까지의 배열이 베스트였다면 결과 저장
                    current.popleft()
                    passOk, minInd, maxInd = check(current[0], i)
                    while(not passOk):
                        current.popleft()
                        passOk, minInd, maxInd = check(current[0], i)
            if nums[maxInd] < nums[i]:
                if nums[i] - nums[minInd] <= limit: #배열이 계속될 수 있을 때
                    maxInd = i
                else: #이전 요소를 버려가며 갱신해야 할 때
                    passOk = False
                    #변경 전, 지금까지의 배열이 베스트였다면 결과 저장
                    current.popleft()
                    passOk, minInd, maxInd = check(current[0], i)
                    while(not passOk):
                        current.popleft()
                        passOk, minInd, maxInd = check(current[0], i)
            maxLen = len(current) if len(current) > maxLen else maxLen
        return maxLen

sol = Solution()
print(sol.longestSubarray(nums = [8,2,4,7], limit = 4))
print(sol.longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
print(sol.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))
