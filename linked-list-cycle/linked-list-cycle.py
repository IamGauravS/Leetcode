# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## if we get None then no cycle if we dont then it's a cycle
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast:
                return True
            
            
            
        return False