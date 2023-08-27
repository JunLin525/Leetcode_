class Solution:
    def isSubsequence(self, s: str, t: str) :
        i, j = 0, 0 # initial two pointer to check this to string
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 #若相同就往後移動一格
            j += 1 #若找不到就把J往後找直到找到跟I相同的
        return i == len(s) #看兩者是否相等，相等就代表S有走到最後，沒有就false