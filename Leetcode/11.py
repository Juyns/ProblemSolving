# 11. Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getArea(l, r):
            return abs(r-l)*min(height[r], height[l])

        left = len(height)//2
        #right = len(height)-left
        l = 0
        r = len(height)-1
        current = getArea(l, r) #양 끝단을 기준으로 시작
        """
            모든 left와 right의 경우에 대해 탐색X, 양 끝을 시작으로 l이나 r이 더 커지는 경우에만 실제 물의 양을 판별
            -> 판별까지 해야함. 가로 너비라는 변수도 존재하기 때문 -> 이후 l과 r교체
        """
        for i in range(left):
            for j in range(len(height)-1, -1, left):
                if height[i] > l:
                    current = max(getArea(height[i], r), getArea(l, r))
                    if height[j] > r:
                        current = max(getArea(l, height[j]), getArea(height[i], height[j]))
                        r = j
                    l = i
                else:
                    if height[j] > r:  
                        current = max(getArea(l, r), getArea(l, height[j]))
                        r = j
        return current

sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))