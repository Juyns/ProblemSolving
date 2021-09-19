# 784. Letter Case Permutation

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        current = []
        if 48 <= ord(s[0]) <= 57:
            current.append(s[0])
        else:
            current.append(s[0].upper())
            current.append(s[0].lower())
        for i in range(1, len(s)):
            if 48 <= ord(s[i]) <= 57:
                for j in range(len(current)):
                    current[j] += s[i]
            else:
                for j in range(len(current)):
                    current.append(current[j] + s[i].upper())
                    current[j] += s[i].lower()
        return current

sol = Solution()
print(sol.letterCasePermutation(s = "asdfwe"))
        