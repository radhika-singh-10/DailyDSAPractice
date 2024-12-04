# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if no head or one node or two nodes->return head #edge case
        #to calculate the length of the linked list and get the last pointer and use last for pointing it
        #cur pointing to current element and its next should be moved to end of last

        if not head or not head.next:
            return head
        temp1=head
        temp2=head.next
        dummy=temp2
        while temp2 and temp2.next:
            temp1.next=temp2.next
            temp1=temp1.next
            temp2.next=temp1.next
            temp2=temp2.next
        temp1.next=dummy
        return head
        # else:
        #     cur,last=head,head
        #     while cur:
        #         if not cur.next:
        #             last=cur
        #         cur=cur.next

        #     cur=head
        #     while cur:
        #         if not cur and not cur.next:
        #             last.next=cur.next
        #             cur.next=cur.next.next
        #             cur=cur.next
        #             print(last.val,cur.val)
        #         cur=cur.next

        #     return head
            