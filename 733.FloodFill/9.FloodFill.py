class Solution:
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        StartingPixel=image[sr][sc]
        self.dfs(image, sr, sc, color, StartingPixel)

        return image

    def dfs(self, image, sr, sc, color, StartingPixel):
        if sr<0 or sr>len(image)-1 or sc <0 or sc > len(image[0])-1 or image[sr][sc] == color or image[sr][sc]!=StartingPixel:
            return
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color ,StartingPixel)
        self.dfs(image, sr-1, sc, color ,StartingPixel)
        self.dfs(image, sr, sc+1, color ,StartingPixel)
        self.dfs(image, sr, sc-1, color ,StartingPixel)


