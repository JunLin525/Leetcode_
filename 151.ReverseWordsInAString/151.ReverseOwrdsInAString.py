class Solution:
    def reverseWords(self, s: str) :
        if s  ==" ": #如果是一個空的，直接回傳。
            return s
        ls = s.split()
        if ls ==[]:# 若是只有一個空格，也直接回傳。
            return ""
        result = ""
        for i in range (0, len(ls)-1):#從最後回傳，然後每次都一個數值並多一個空格。
            result += ls[len(ls)-1-i]+" "
        result += ls[0] #怕多一個空格，所以把第一個單獨回傳
        return result