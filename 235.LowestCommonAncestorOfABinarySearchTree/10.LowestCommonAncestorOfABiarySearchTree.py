# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pointer = root
        while pointer:
            if p.val > pointer.val and q.val > pointer.val: #如果都比較大就往右邊跑
                pointer = pointer.right
            elif p.val < pointer.val and q.val < pointer.val:# 如果都比較小就往左跑
                pointer=pointer.left 
            else: #剛好介於中間就回傳本身
                return pointer