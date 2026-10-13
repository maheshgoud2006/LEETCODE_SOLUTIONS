# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head 
        temp=dummy
        while temp.next is not  None and temp.next.next is not None:
            first=temp.next
            second = temp.next.next

            first.next=second.next
            second.next=first
            temp.next=second
            temp=first

        return dummy.next




        










        



        