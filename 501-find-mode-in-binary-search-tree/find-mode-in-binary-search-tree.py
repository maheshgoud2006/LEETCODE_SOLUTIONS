# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        nums = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        result=[]
        maximum=0

        for i in nums:
            count=nums.count(i)

            if count>maximum:
                maximum=count
                result=[i]
            elif count==maximum and i not in result:
                result.append(i)

        return result 









        