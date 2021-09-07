# 3. Longest Substring Without Repeating Characters

class Solution:
    def testString(self, num, alp):
        """
            현재까지의 문자열들을 나타낸 정수 num과 안에 있는지 테스트할 문자 alp를 받음
            alp에 해당하는 binary index가 이미 존재하면 return true
            현재까지의 인덱스보다 큰 인덱스를 할당받아야 하거나, binary index가 존재하지 않으면 return False
        """
        toTest = bin(num)[2:]
        ind = ord(alp) if alp != ' ' else 32 #공백이 들어왔을 경우 처리가 안 되기에 이와 같이 설정해줌.
        if ind >= len(toTest): return False
        if toTest[len(toTest)-1-ind] == '1': return True
        return False
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s) #길이가 0이거나 1이면 최대 길이 = string길이
        leng = 1
        maxLen = 0 #현재까지의 최대 길이
        left, right = 0, 1
        current = 2**ord(s[left]) if s[left] != ' ' else 2**32 #현재 배열을 이진수로 나타냄. ex. ac = 101(그냥 예시용)
        while (left <= right and right < len(s)):
            """
                1. testString함수로 점검하여 이미 존재하면 left index를 한 칸 이동해줌.
                이후 바로 다음 loop에서 다시 right index 존재여부 점검
                2. 존재하지 않으면 현재 number에 더해주고 maxLen 갱신
            """
            if self.testString(current, s[right]): 
                current -= 2**ord(s[left]) if s[left] != ' ' else 2**32 #
                leng -= 1
                left += 1
                continue
            current += 2**ord(s[right]) if s[right] != ' ' else 2**32
            leng += 1
            right += 1
            maxLen = max(leng, maxLen)
        return maxLen

sol = Solution()
print(sol.lengthOfLongestSubstring(s = "d"))  