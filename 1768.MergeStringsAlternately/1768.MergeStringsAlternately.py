class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        # Init
        size1 = len(word1)
        size2 = len(word2)
        mergeWord = []

        # Merge
        i, j = 0, 0
        while i < size1 and j < size2:
            mergeWord.append(word1[i])
            mergeWord.append(word2[j])
            i+=1
            j+=1
        
        mergeWord.append(word1[i:])
        mergeWord.append(word2[j:])

        return "".join(mergeWord)