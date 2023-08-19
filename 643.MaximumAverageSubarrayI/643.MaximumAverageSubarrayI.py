class Solution:
    def findMaxAverage(self, nums: List[int], k: int) :
        tmp = 0 
        result =float('-inf')
        for i, x in enumerate(nums):
            