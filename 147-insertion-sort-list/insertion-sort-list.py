# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sorted_list=None
        temp=head
        while temp:
            curr=temp
            temp=temp.next
            if sorted_list is None or curr.val < sorted_list.val:
                curr.next=sorted_list
                sorted_list=curr
            else:
                p=sorted_list
                while p.next and p.next.val <= curr.val:
                    p=p.next
                curr.next=p.next
                p.next=curr
        return sorted_list
        





       