# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
#         c= 1
#         node = head
#         while node.next:
#             c += 1
#             node = node.next
        
#         print(c)
#         c = ceil(c/2)
#         print(c)
#         ci = 0
#         node = head
#         while True:
#             if ci == c-2:
#                 print(node.val)
#                 node.next = node.next.next
#                 break
#             else:
#                 ci +=1
#                 node = node.next
#         return head
        