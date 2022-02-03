#1177. Can Make Palindrome from Substring - LeetCode Medium


from typing import List
import math

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        charFreq=[0b0 for _ in range(len(s))]
        for i in range(0, len(s)):
            toCalc = 2**(ord(s[i])-97)
            charFreq[i] = int(bin(charFreq[i-1]^toCalc), 2) if i != 0 else toCalc

        def divideWord(s, left, right, k):  
            limOdd=2*k
            if (right+1-left)%2 == 1: limOdd += 1
            target = charFreq[right]^charFreq[left-1] if left != 0 else charFreq[right]
            i = 0
            while(target != 0):
                target&=target-1
                i+=1
            return limOdd-i >= 0


        results=[]
        for left, right, k in queries:
            results.append(divideWord(s, left, right, k))
        return results

a = Solution()
print(a.canMakePaliQueries( s = "nafqfybodkha", queries = [[11,11,1],[4,11,2],[1,8,7],[2,11,1],[3,4,0],[8,11,4],[5,8,2],[6,7,2],[11,11,1],[8,11,4],[5,8,2],[10,11,2],[7,11,3],[4,7,0],[9,10,1],[10,11,1],[3,8,0],[0,7,8],[1,2,1]]))
print(a.canMakePaliQueries( s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
print(a.canMakePaliQueries( s = "abcda", queries = [[0,4,1]]))