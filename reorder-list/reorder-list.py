# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## find the midpoint of the list
        slow, fast = head, head.next 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        second = slow.next ##starting point of second half
        prev = None
        slow.next = None
        ## reverse the half of linked list
        while second:
            tmp = second.next 
            second.next = prev
            prev = second
            second = tmp 
            
        ## merge the two half
        ## after the loop stops executing second is null and prev is the last node
        second = prev 
        first = head 
        
        while second:
            tmp1 , tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1 
            first = tmp1 
            second = tmp2 
            
        
            