class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] *(n+1)   # 有N+1個數字(含0)
        offset = 1 #從一開始，offset=1 每次最高位元有突破的時候 1 2 4 8 16 就會變化

        for i in range(1,n+1):
            if offset*2 == i:
                offset =i
            dp[i]=1+dp[i-offset]
        return dp