class Solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            j=target -i
            startIndex=nums.index(i)
            nextIndex=startIndex+1
            newNums=nums[nextIndex: ]
            if j in newNums:
                return(startIndex, nextIndex+newNums.index(j))