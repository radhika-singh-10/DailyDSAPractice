# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur=None
        #swapping by using two variables
        while head and head.next:
            temp=head.next
            head.next=cur
            cur=head
            head=temp
            #head=head.next
            print(cur.val,head.val)
        head.next=cur
        return head
        
        