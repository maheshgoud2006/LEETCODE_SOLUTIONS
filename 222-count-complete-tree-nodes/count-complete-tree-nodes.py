# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0
        left=root.left
        right=root.right

        lt=rt=0
        while left:
            lt+=1
            left=left.left
            
        while right:
            rt+=1
            right=right.right
        if lt==rt:
            return (2 ** (rt + 1)) - 1
        
        return 1+ self.countNodes( root.left) +self.countNodes(root.right)

        


        