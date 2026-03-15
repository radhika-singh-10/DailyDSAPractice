# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#approach
#one external loop for checking on each node
#internal loop for replacing the unsorted elem
#outer loop logic
#node.val>node.next.val
#replace=node.next
#node.next=node.next.next
#internal loop logic
#if temp.next.val>replace.val
#replace.next=temp.next.next
#temp.next=replace

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy=ListNode()
        node=head
        while node:
            prev=dummy
            while prev and prev.next and prev.next.val<=node.val:
                prev=prev.next
            nextElem=node.next
            node.next=prev.next
            prev.next=node
            node=nextElem
        return dummy.next

