# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #no cycles, no sorting present
        temp_one,temp_two=headA,headB
        while temp_one!=temp_two:
            temp_one=headB if temp_one is None else temp_one.next
            temp_two=headA if temp_two is None else temp_two.next
        return temp_one