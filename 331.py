# 331. Verify Preorder Serialization of a Binary Tree

class Solution(object):
    def isValidSerialization(self, preorder):
        def rec(currentInd):
            if currentInd >= len(preorder): return -1
            done[currentInd] = True
            if preorder[currentInd] == '#':
                return currentInd
            left = rec(currentInd+1) # Left
            if left != -1:
                right = rec(left+1)
                if right != -1: return right
            return -1
        preorder = preorder.split(',')
        done = [False for _ in range(len(preorder))]
        if rec(0) == -1: return False
        for comp in done:
            if not comp: return False
        return True

sol = Solution()
print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

print(sol.isValidSerialization("1,#"))

print(sol.isValidSerialization("9,#,#,1"))

                        
                
        