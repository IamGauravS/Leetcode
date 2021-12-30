# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            ## save ptrs
            nxtPair = curr.next.next 
            second  = curr.next 
            
            ## reverse
            second.next = curr
            curr.next = nxtPair
            prev.next = second 
            
            ## update
            prev = curr  ## current has moved one place here thats why
            curr = nxtPair
            
            
        return dummy.next