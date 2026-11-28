class Solution(object):
    def minDiffInBST(self, root):
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        ans = float('inf')

        for i in range(1, len(values)):
            diff = values[i] - values[i-1]
            ans = min(ans, diff)

        return ans