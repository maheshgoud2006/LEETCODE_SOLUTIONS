# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        path=[]
        result=[]
        def dfs(root):
            if root is None:
                return
            path.append(str(root.val))

            if root.left is None and root.right is None:
                result.append("->".join(path))

            dfs(root.left)
            dfs(root.right)
            path.pop()

        dfs(root)

        return result




        