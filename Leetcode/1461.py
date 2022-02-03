# 1461. Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        left = 0;
        offset = k
        dp = [False for i in range(2**k)]
        while(left+offset <= len(s)):
            dp[int(s[left:left+offset], 2)] = True
            left += 1
        for i in range(2**k):
            if not dp[i]: return False
        
        return True

sol = Solution()
print(sol.hasAllCodes(s = "00110", k = 2))