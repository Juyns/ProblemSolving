class Solution(object):
    def prevPermOpt1(self, arr):
        ind = len(arr)-1
        while ind > 0 and arr[ind-1] <= arr[ind]:
            ind = ind-1
        if ind > 0:
            toChange = ind-1
            for i in range(ind, len(arr)):
                if arr[toChange] > arr[i] > arr[ind]:
                   ind = i
            arr[ind], arr[toChange] = arr[toChange], arr[ind]
        return arr
        
sol = Solution()

print(sol.prevPermOpt1([1,9,4,6,7]))
print(sol.prevPermOpt1([3,1,1,3]))
print(sol.prevPermOpt1([3,1,21]))
print(sol.prevPermOpt1([1,1,9,4,9,7,7,5,3,10,4,10,2,3,4,9,4,6,5,10,7,2,9,4,10,7,10,5,10,9,5,3,6,9,3,1,2,9,1,4,5,1,3,2,10,7,9,6,9,6,9,9,1,8,7,8,9,5,9,8,6,1,10,9]))
