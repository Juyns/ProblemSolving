#106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        rootIndex = 0
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                rootIndex = i
                break
        rootLeft = self.buildTree(inorder[:rootIndex], postorder[:rootIndex]) if rootIndex != 0 else None
        rootRight = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:len(inorder)-1]) if rootIndex+1 <= len(inorder)-1 else None
        root = TreeNode(inorder[rootIndex], rootLeft, rootRight)
        return root 

# 얘는 모범풀이 다시보기
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/1114837/Python3-faster-than-93-with-hash-recursive-solution 