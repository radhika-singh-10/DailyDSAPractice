class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val<=self.minStack[-1]:
            self.minStack.append(val)
        
    def pop(self) -> None:
        if self.minStack[-1]==self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()
          
    
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# class MinStack:

#     def __init__(self):
#         self.stack=[]
#         self.minstack=[]

#     def push(self, val: int) -> None:
#         if self.stack:
#             self.stack.append(val)
#             val = min(val , self.minstack[-1] if self.minstack else val)
#             self.minstack.append(val)

#     def pop(self) -> None:
#         if self.stack:
#             v=self.stack.pop()
#             v=self.minstack.pop()

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]
#         else:
#             return -1

#     def getMin(self) -> int:
#         if self.stack:
#             return self.minstack[-1]
#         else:
#             return -1


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()