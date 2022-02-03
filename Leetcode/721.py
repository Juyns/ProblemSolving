# 721. Accounts Merge 모범답안 

from typing import List
from collections import defaultdict

#유니온파인드 클래스
class UF:
    def __init__(self, N):
        self.parents = list(range(N)) # parent = [0~~len(accounts)-1]
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent) # owner a와 b를 받았을 때, b의 부모의 부모를 a의 부모로 설정 
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {} #email-소유주(인덱스)로 구성된 dictionary
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership: 
                    uf.union(i, ownership[email]) #email중에서 이미 소유주가 정의된 email이 있는 경우 -> 현재 component에 있는owenr a와  이미 존재하던 owner b를 합쳐줘야 한다.
                ownership[email] = i # 일단 ownership은 있는 대로 두는 것. 어차피 UF instance의 parents에 부모 정보가 저장되니까

        # Append emails to correct index
        ans = defaultdict(list) #defaultdict는 value의 기본값이 매개변수(여기서는 list)로 설정됨.
 
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email) #ownership에는 중복되지 않는 모든 email과 email의 가장 최근 소유주가 담겨있다. 이 각각의 email들에 대해 가장 상단의 부모-email쌍으로 ans에 저장

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

sol = Solution()
print(sol.accountsMerge(accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))