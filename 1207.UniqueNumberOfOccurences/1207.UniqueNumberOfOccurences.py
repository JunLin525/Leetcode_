class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={} #建立一個dict
        for num in arr: #掃一輪arr 裡面的數值
            if num not in dict: #不在裡面的話就把值令成1
                dict[num] = 1
            else:# 若在裡面的話就+1
                dict[num]+=1
        return len(dict.values()) ==len(set(dict.values())) #若沒有相同的話，長度不會變短，來判斷有沒有重複