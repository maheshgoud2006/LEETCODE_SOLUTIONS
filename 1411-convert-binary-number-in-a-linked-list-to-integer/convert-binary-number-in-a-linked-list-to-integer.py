# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if head is None :
            return 0
        temp= head
        number=0
        while temp is not None:
            number =number*2+temp.val
            temp=temp.next
        return number


        

        