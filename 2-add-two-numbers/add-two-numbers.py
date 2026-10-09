# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        current=dummy
        carry=0
        while l1 or l2 or carry:

            x=0
            y=0
            if l1:
                x=l1.val
            if l2:
                y=l2.val
            total=x+y+carry

            digit=total%10
            carry=total//10
            newnode=ListNode(digit)
            current.next=newnode
            current=current.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next


            



            



            
            

            