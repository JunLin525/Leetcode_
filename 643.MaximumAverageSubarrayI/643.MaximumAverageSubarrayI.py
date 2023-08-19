class Solution:
    def findMaxAverage(self, nums: List[int], k: int) :
        tmp =0
        result =float('-inf')

        for i, x in enumerate(nums): #I是位置、X代表數值
            tmp += x
            if i>=k: #當超出K格時候，扣掉初始位置的那些值
                tmp -= nums[i-k]
            if i>=k-1: # 當剛好的時候，就找最大值
                result=max(result,tmp)
        return result/k #回傳