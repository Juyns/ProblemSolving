# 464. Can I Win


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal: return False
        memo = {}
        done = [False for _ in range(maxChoosableInteger+1)]
        # 기본적으로, dfs에서는 자기 턴에서 예측함. dfs함수로 턴을 잡았을 때, 현 상태에서 이길 수 있으면 true / 못 이기면 false
        def dfs(total, isDone):
            if tuple(isDone) in memo: return memo[tuple(isDone)]
            for num in range(1, maxChoosableInteger+1):
                if isDone[num]: continue
                if total + num >= desiredTotal:
                    memo[tuple(isDone)] = True
                    return True # 현 상태에서 이길 수 있는 상태라면? 바로 true 리턴
                else: # 현 num으로 이길 수 없으면 일단 고른다음에 다음 턴 예측해보기 
                    isDone[num] = True
                    if not dfs(total+num, isDone): #다음 턴에서 상대가 진다는 결과가 나오면? true
                        isDone[num] = False
                        memo[tuple(isDone)] = True
                        return True
                isDone[num] = False
            # 현 상태에서 모든 경우를 시도해봤지만 이기지 못 할 경우
            memo[tuple(isDone)] = False
            return False
        return dfs(0, done)

sol = Solution()
print(sol.canIWin(10,40))  
