class Solution:
    def isAnagram(self, s: str, t: str) :

        lookup ={}
        ##建立一個表存取string s 裡面的次數跟字母
        for i in s:
            if i not in lookup:
                lookup[i]=1
            else:
                lookup[i]+=1
        ##檢查J有沒有在S的檢查表中，若出現沒有的字母就直接錯啦
        for j in t:
            if j not in lookup:
                return False
            else:
                lookup[j]-=1
        # 檢查是不是都歸零了
        for k in lookup:
            if lookup[k] != 0:
                return False
        ## 上面邏輯都通過了 就給你True
        return True