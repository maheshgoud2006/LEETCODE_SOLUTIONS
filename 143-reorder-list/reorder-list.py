# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow=head
        fast=head
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
        

        curr=slow.next
        slow.next=None
        prev=None

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        first=head
        second=prev

        while second:


        
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2




            