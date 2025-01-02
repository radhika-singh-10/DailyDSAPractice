class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #sorted list -> rotated -> good approach - binary search
        #edge cases-> int, negative, fraction?
        #no element -> false, 1 ele->check if mathces with target
        #formula- check for rotation
        #m==target->true else false
        #if m<=target -> if l<=target<=m r=m-1 else l=m+1
        #else -> if m<=target<=r->l=m+1 else r=m-1

        #[2,5,6,0,0,1,1,2,2] target=6
        n=len(nums)
        if not nums:
            return False
        if n==1:
            if target==nums[0]:
                return True
            else:
                return False
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[m]:
                if nums[l]<=target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[m]<=target<=nums[r]:
                    l=m+1
                else:
                    r=m-1

        return False

