# 1963. Minimum Number of Swaps to Make the String Balanced

class Solution(object):
    def minSwaps(self, s):
        i = 0;
        stack = []
        if len(s) == 0: return 0
        while i < len(s):
            if s[i] == '[':
                stack.append(s[i])
            else:
                if stack: stack.pop()
            i += 1
        return (len(stack) + 1) // 2 # 남은 모든 [ 는 ] 보다 오른쪽에 있을 것. 그럼 양 끝단의 한 쌍을 바꾸면 왼쪽과 오른쪽 각각의 bracket이 하나씩 추가로 처리된다.

            
sol = Solution()
print(sol.minSwaps(s ="]]][[["))


# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
