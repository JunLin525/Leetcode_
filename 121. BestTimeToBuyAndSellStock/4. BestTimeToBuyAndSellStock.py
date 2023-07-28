class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minPrice  =float("inf")

        for price in prices:
            minPrice  = min(price, minPrice)
            maxProfit = max(maxProfit, price-minPrice)

        return maxProfit