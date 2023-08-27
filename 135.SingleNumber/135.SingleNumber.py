class Solution:
    def singleNumber(self, nums: List[int]):
        res = 0 
        for n in nums:
            res = n ^ res # xor 相同的就會歸零，不同的就會變成一，最後回傳那個一的2進位數直。
        return res