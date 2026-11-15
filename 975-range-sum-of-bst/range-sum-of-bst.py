# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        def order(root):
            if root is None:
                return 0
            if low<=root.val<=high:
                current= root.val
            else:
                current=0
            left=order(root.left)
            right=order(root.right)
        
            return left+ right+current
        return order(root)








        