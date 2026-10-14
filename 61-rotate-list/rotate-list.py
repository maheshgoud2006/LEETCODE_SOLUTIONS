
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find the length of the linked list
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Connect the tail to the head to form a circle
        tail.next = head

        # Find the new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
