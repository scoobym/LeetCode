# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    i = 0
    temp = None
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root.left != None:
            self.midOrder(root.left, k)
        if self.i == k :
            return self.temp.val
        elif self.i == k-1 :
            return root.val
        else :
            self.i += 1
            self.midOrder(root.right, k)
            return self.temp.val
            
            
    def midOrder(self, root, k):
        if root!=None and root.left != None :
            self.midOrder(root.left, k)
        self.i += 1
        if self.i==k:
            self.temp = root
        elif root!=None and root.right != None :
            self.midOrder(root.right, k)
        