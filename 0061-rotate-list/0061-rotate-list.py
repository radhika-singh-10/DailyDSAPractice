# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #edge case -> head, head.next -null, 0,1 elem, k=0(same list)
        #approach->find the length, edge - if k%l ==0, return same list
        #k=k%l steps-k-l-1 => new-_tail=new_tail.next => new_head=new_tail.next
        #new_tail.next=None tail.next=head  
        #new_head
        if not head or not head.next or k == 0:
            return head
        total_nodes = 1
        tail = head
        while tail.next:
            tail = tail.next
            total_nodes += 1
        k = k % total_nodes
        if k == 0:
            return head  
        steps = total_nodes - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        tail.next = head
        new_tail.next = None
        
        
        return new_head