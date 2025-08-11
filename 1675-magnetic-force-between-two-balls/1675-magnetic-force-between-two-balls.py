class Solution:
    #kok eating banana problem pattern
    def isBallPlaced(self,x,position,m,n):
        prev,placement=position[0],1
        for i in range(1,n):
            cur=position[i]
            if cur-prev>=x:
                placement+=1
                prev=cur
            if placement==m:
                return True
        return False
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n,res=len(position),0
        l,r=1,int(position[-1]/(m-1.0))+1
        while l<=r:
            mid=l+(r-l)//2
            if self.isBallPlaced(mid,position,m,n):
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res



