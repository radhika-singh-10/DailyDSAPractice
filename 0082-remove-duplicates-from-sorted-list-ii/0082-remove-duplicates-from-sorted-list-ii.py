# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None
        # if head==None or head.next==None:
        #     return head
        sentinel = ListNode(0, head)
        pred = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinel.next


        # if head.val==head.next.val:
        #     while head.val!=head.next.val:
        #         head=head.next
        #     head=head.next
            
        # temp=head
        # while temp.next!=None:
        #         if temp.val==temp.next.val:
        #             temp.next=temp.next.next
        #         else:
        #             temp=temp.next
        # return head
            