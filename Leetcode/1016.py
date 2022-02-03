# 1016. Binary String With Substrings Representing 1 To N

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if int(s, 2) == 0: return False
        def check(num):
            start = 0
            offset = len(bin(num))-2
            while(start+offset <= len(s)):
                if s[start:start+offset] == bin(num)[2:]: return True
                start += 1
            return False

        for i in range(2, n+1):
            if not check(i):
                return False
            
        return True



sol = Solution()
print(sol.queryString(s = "11100000011101000000101010000100001001100000000101100011101101010100011010101100010010001001100101100011011110101011000110011011101110000111100001111111000101011110110101110110101001011010100110001001", n = 10))
