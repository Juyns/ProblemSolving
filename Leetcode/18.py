# 18. 4Sum /모범답안임
class Solution():
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result):
            length = r - l + 1
            if length < N or N < 2:
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]): # i가 이전 요소와 중복된 채로 findNsum에 들어가면 리스트 중복 발생
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]])

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [])
        return results