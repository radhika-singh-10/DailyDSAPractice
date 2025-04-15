# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #siumilar to reverse linkedlist logic
        newHead=ListNode(0)
        newHead.next=head
        prev,slow=newHead,head
        while slow:
            if slow.val==val:
                prev.next=slow.next
            else:
                prev=slow
            slow=slow.next
        return newHead.next
        