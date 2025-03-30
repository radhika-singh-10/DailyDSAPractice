# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head,k):
        if not head:
            return head
        prev,cur=None,head
        while k:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            k-=1
        return prev
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        #head=self.reverseLinkedList(head)
        #take a counter and pass offset and offset+kth node
        #apply reverse logic there
        temp,offset=head,0
        while offset<k and temp:
            offset+=1
            temp=temp.next
        if offset==k:
            revHead=self.reverseLinkedList(head,k)
            head.next=self.reverseKGroup(temp,k)
            return revHead

        return head
        