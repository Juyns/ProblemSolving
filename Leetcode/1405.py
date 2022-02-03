class Solution(object):
    def longestDiverseString(self, a, b, c):
        alps = {'a' : a, 'b' : b, 'c' : c}
        lastAlp = ''
        word = ""
        s = sorted(alps.items(), key=lambda x: x[1], reverse=True)
        while True:
            s = sorted(alps.items(), key=lambda x: x[1], reverse=True)
            toAddAlp = s[0][0]
            if toAddAlp == lastAlp:
                if len(word) > 1 and word[-1] == word[-2]:
                    toAddAlp = s[1][0] #두번째로 많은거로 변경
            if alps[toAddAlp] < 1: break
            word += toAddAlp
            lastAlp = toAddAlp
            alps[toAddAlp] -= 1
        return word

        
sol = Solution() 
print(sol.longestDiverseString(7,1,0))