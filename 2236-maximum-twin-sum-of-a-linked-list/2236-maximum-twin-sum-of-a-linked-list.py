# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        res=-float("inf")
        fast,slow=head,head
        stack=[]
        while fast and fast.next:
            fast=fast.next.next
            stack.append(slow.val)
            slow=slow.next
        
        
        while slow:
            res=max(res,stack.pop()+slow.val)
            slow=slow.next

        return res

        