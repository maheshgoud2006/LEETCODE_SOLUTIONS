# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        bfs=[root]
        result=[]
        left_to_right=True

        while bfs:
            level=[]
            l=len(bfs)
            for  i in range(l):
                node = bfs.pop(0)
                level.append(node.val)

                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

            if left_to_right:
                result.append(level)
            else:
                result.append(level[::-1])
            left_to_right= not left_to_right
        return result

                
                






        
        