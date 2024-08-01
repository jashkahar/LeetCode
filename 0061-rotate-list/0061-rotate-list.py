# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate the length of the list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Step 2: Normalize k
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the new tail
        new_tail_position = length - k - 1
        new_tail = head
        for _ in range(new_tail_position):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        # Step 4: Update pointers
        current.next = head

        return new_head
        

        