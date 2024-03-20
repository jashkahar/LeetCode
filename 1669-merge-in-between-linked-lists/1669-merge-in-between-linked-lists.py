# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy1 = list1
        
        start = ListNode()
        end = ListNode()
        nextstart = ListNode()
        
        c = 0
        
        while c<b:
            if c == a-1:
                start = list1
            c+=1
            list1 = list1.next
        start.next = list2
        
        while list2:
            if not list2.next:
                # print(list2.val)
                list2.next = list1.next
                break
            list2 = list2.next            
        # print(list1.val)
        # list2 = list1.next
        list1.next = None
        
        return dummy1
        
        
        
            
            
        