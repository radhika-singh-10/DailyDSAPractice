# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #first_ptr,second_ptr = head, head.next
        #first_p=first_pt.next,second_pt=second_pt.next
        #while not first_ptr:
        #. first_p=first_pt.next,second_pt=second_pt.next
        #. if not second_ptr:
        #     second_ptr.next=head
        #.    first_ptr.next=None
        #. k-=1
        if not head or not head.next or k == 0:
            return head
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        k = k % l
        if k == 0:
            return head  
        steps = l - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head