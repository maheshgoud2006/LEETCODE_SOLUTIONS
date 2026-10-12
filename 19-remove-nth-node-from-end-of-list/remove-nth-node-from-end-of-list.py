# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next
        k=c-n
        temp=head 
        if k==0:
            return head.next
        temp=head
        while k>1:
            temp=temp.next
            k-=1
        temp.next=temp.next.next
        return head


        