#Flip String to Monotone Increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        origin = int("0b"+s, 2)
        trim = bin(origin)
        zeroCount = len(trim)-2
        
        while origin != 0:
            if bin(origin ^ 1)[-1] == '0':
                zeroCount -= 1
            origin = origin >> 1
        fixToOne = zeroCount
        makeZero = 0
        for comp in trim[2:]:
            if comp == '0':
                zeroCount -= 1
            if comp == '1':
                fixToOne = min(makeZero + zeroCount, fixToOne)# 현재 있는 걸 1로 바꾸고 나머지 앞에것들은 0으로, 뒤에는 1로 고정 vs 이전에 고정했던 대로 그냥 두기
                makeZero += 1
            #print(comp, fixToOne, makeZero)

        return min(makeZero, fixToOne)                
            
                
sol = Solution()
print(sol.minFlipsMonoIncr(s="00011000"))