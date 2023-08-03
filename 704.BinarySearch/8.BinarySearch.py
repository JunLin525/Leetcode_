class Solution:
    def search(self, nums: List[int], target: int) :
        l, r = 0, len(nums)-1
        while l<=r:
            m=l+ ((r-1)//2) ## 怕直接相加除二會overflow故用算距離的方式來處理。
            if nums[m] > target:
                r=m-1
            elif nums[m] <target: 
                l=m+1
            else:
                return m
        
        return -1 #若找不到 回傳-1