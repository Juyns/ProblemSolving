# 456. 132 Pattern

class Solution(object):
    def find132pattern(self, nums):
        if len(nums) < 3: return False
        m_stack = [nums[0]]
        for i in range(len(nums)):
            m_stack.append(min(nums[i], m_stack[-1]))
        mid = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= m_stack[i]: continue
            while mid and mid[-1] <= m_stack[i]: mid.pop()
            if mid and m_stack[i] < mid[-1] < nums[i]: return True
            mid.append(nums[i])
        return False
    
sol = Solution()
print(sol.find132pattern(nums = [-1,3,2,0]))
    