# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy_head = ListNode(0)  
        temp = dummy_head
        t1=l1
        t2=l2
        while t1 or t2 or carry:
            v1=t1.val if t1 else 0
            v2=t2.val if t2 else 0
            total=v1+v2+carry
            carry=total//10
            temp.next=ListNode(total%10)
            temp=temp.next
            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
            
        return dummy_head.next

        # while t1 and t2:
        #     t1.val+=t2.val+carry
        #     if t1.val>9:
        #         carry=int(t1.val/10)
        #         t1.val%=10
                
        #     t1=t1.next
        #     t2=t2.next
        # while t2:
        #     t1.next=t2
        #     t1.val+=carry
        #     print(t1.val,carry,t2.val)
        #     if t1.val>9:
        #         carry=int(t1.val/10)
        #         print(t1.val,carry,t2.val)
        #         t1.val%=10
        #     t2=t2.next
        #     t1=t1.next

        # while t1:
        #     t1.val+=carry
        #     print(t1.val,carry)
        #     if t1.val>9:
        #         carry=int(t1.val/10)
        #         print(t1.val,carry)
        #         t1.val%=10
        #     t1=t1.next
        
        # if carry==1:
        #     new=ListNode()
        #     new.val=carry
        #     print(carry,new.val)
        #     t1=new
        #     t1.val=new.val
        
        # return l1

