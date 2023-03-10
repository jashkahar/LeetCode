# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         return

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        
        current_node = self
        
        while current_node is not None:
            print(current_node.val, end='')
            print("-->", end='')
            
            # jump to the linked node
            current_node = current_node.next            
        return        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lists_sum = l1, l2
        dummy = cur = ListNode(0)
        carry = 0
        while lists_sum or carry:
            carry += sum(item.val for item in lists_sum)
            lists_sum = [item.next for item in lists_sum if item.next]
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry /= 10
            carry = int(carry)
        return dummy.next