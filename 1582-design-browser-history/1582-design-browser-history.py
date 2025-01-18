class BrowserHistory:
    #double linked list - Link
    #val:string, next:Links, prev
    #1. assign the value of homepage
    #2. visit- check if linkedin list is empty, if yes-> assign the value
    #no then traverse and assign the value
    #3. back - we use prev pointer to traverse and locate the step
    #4. forward - we use next pointer
    class Link:
        def __init__(self, val: str):
            self.val = val
            self.next = None
            self.prev = None
    
    def __init__(self, homepage: str):
        self.cur = self.Link(homepage)
        
    def visit(self, url: str) -> None:
       new_link = self.Link(url)
       self.cur.next=new_link
       new_link.prev = self.cur
       self.cur=new_link


    #what if steps>total length??
    def back(self, steps: int) -> str:
        while steps>0 and self.cur.prev:
            self.cur=self.cur.prev
            steps-=1
            
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        while steps>0 and self.cur.next:
            self.cur=self.cur.next
            steps-=1
            
        return self.cur.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)