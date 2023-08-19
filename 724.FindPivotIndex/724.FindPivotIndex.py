class Solution:
    def pivotIndex(self, nums: List[int]):
        l, r = 0,sum(nums)
        for i in range(len(nums)):
            r-=nums[i] # 這樣放避免一開始就達成，左右都是0
            if l == r: return i 
            l +=nums[i] #不行就左邊開始累加 跟右邊累減一起比對
        return -1