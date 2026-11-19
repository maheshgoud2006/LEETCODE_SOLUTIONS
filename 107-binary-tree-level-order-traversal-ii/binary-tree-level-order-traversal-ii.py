# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        dfs=[root]
            
        result=[]

        while dfs:
            l=len(dfs)
            level=[]
                
            for i in range(l):
                node=dfs.pop(0)
                level.append(node.val)
                    
                if node.left:

                    dfs.append(node.left)
                if node.right:

                    dfs.append(node.right)

            result.append(level)
        result.reverse()
        return result


                




        