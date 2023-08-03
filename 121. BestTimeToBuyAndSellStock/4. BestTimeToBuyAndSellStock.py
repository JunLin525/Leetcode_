class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MaxProfit, MinPrice=0, float("inf") ##先設定為無限，後面再變小
        for price in prices:
            MinPrice  = min(MinPrice, price) # 比較兩者取其小，找到好的最小值
            MaxProfit = max(MaxProfit, price-MinPrice) # 比較兩者取其大，找到新的最大值

        return MaxProfit