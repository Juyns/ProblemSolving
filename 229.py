class Solution(object):
    def majorityElement(self, nums):
        cand1, cand2, count1, count2 = -1, 1, 0, 0
        mem = len(nums)//3
        for n in nums:
            if n == cand1: count1 += 1
            elif n == cand2: count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 = 1
            elif count2 == 0:
                cand2 = n
                count2 = 1
            else:
                count1 -= 1 
                count2 -= 1
        lst = []
        if nums.count(cand1) > mem: lst.append(cand1)
        if nums.count(cand2) > mem: lst.append(cand2)
        return lst
            
            


sol = Solution()
print(sol.majorityElement(nums=[-1,2,6,2,2,-1,6,-1]))