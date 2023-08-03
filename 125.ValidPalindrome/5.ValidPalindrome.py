class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, (len(s)-1)  # 設定指標，最左邊跟最右邊

        while i<j: # 只要i、j沒有交叉，就繼續比
            while i< j and not s[i].isalnum(): #isalnum可以辨識這個string是不是用數字跟英文字組成，若他不是就會執行下面的+1
                i+=1
            while i<j and not s[j].isalnum():#isalnum可以辨識這個string是不是用數字跟英文字組成，若他不是就會執行下面的+1
                j-=1
            if s[i].lower()!=s[j].lower(): #整理成一樣的小寫，用upper也是可以，但我喜歡用lower。
                return False # 若中間有不同的話，直接False
            i+=1
            j-=1
        return True #最後一步都一致，直接給True
                