"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        old={}
        current=head

        while current is not None:
            old[current]=Node(current.val)
            current=current.next

        current=head
        while current is not  None:
            copy=old[current]

            if current.next is not None:
                copy.next=old[current.next]

            if current.random is  not None:
                copy.random=old[current.random]
            current = current.next
        return old[head]








        