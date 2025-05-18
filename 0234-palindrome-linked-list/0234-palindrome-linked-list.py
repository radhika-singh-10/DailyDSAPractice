# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front=head
        def checkPalindrome(cur):
            if cur:
                if not checkPalindrome(cur.next):
                    return False
                if cur.val!=self.front.val:
                    return False
                self.front=self.front.next
            return True
        return checkPalindrome(head)
                
        