class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr=0
        for i in range(len(nums)): ## 若是他不是0的時候就放進去
            if nums[i]:
                nums[ptr]=nums[i]
                ptr+=1  ##指標每次往前移一個
        for i in range(ptr,len(nums)):##最後把零補在最後面
            nums[i]=0

        return nums