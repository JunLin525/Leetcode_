class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0 #一開始零就是最大的
        curr_alt = 0 #爬坡中間的數值
        for i in gain :
            curr_alt += i
            max_altitude= max(curr_alt ,max_altitude ) #比大小後取代
        return max_altitude