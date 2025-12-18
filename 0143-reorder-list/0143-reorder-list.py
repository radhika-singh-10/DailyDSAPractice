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

        #middle element - fast and slow
        #reverse 2nd list
        #merge the two list

        if not head:
            return head
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
    
        prev,cur=None,slow
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            
        
        first,second=head,prev
        while second.next:
            first.next,first=second,first.next
            second.next,second=first,second.next

        
        