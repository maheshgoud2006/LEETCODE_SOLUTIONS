
class Solution(object):
    def rangeSumBST(self, root, low, high):

        def order(node):
            if node is None:
                return 0

            if node.val < low:
                return order(node.right)

            if node.val > high:
                return order(node.left)

            return (node.val +
                    order(node.left) +
                    order(node.right))

        return order(root)
