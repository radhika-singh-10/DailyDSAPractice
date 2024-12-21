# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #no cycles, no sorting present
        hash_set=set()
        cur=headA
        while cur:
            hash_set.add(cur)
            cur=cur.next
        
        cur = headB
        while cur:
            if cur in hash_set:
                return cur
            cur=cur.next

        return None

        