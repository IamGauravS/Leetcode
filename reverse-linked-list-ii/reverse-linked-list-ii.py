# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        prev, cur = dummy, head
        
        for i in range(left-1):
            prev, cur = cur, cur.next
            
        ## right - left + 1
        
        leftprevious = prev ## saving prev 
        
        prev = None
        for i in range(right-left+1):
            tmpNext = cur.next 
            cur.next = prev
            prev, cur = cur, tmpNext
            
            
        leftprevious.next.next = cur 
        
        leftprevious.next = prev 
        
        return dummy.next 