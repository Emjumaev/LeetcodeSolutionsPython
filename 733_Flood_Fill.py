class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.sColor = image[sr][sc]

        self.dfs(image, sr, sc, color)

        return image
    
    def dfs(self, image: List[List[int]], sr: int, sc: int, color: int):

        if sr < 0 or sr >= len(image):
            return
        
        if sc < 0 or sc >= len(image[0]):
            return

        if image[sr][sc] != self.sColor or image[sr][sc] == color:
            return

        if image[sr][sc] == self.sColor:
            image[sr][sc] = color
        
        self.dfs(image, sr + 1, sc, color)
        self.dfs(image, sr - 1, sc, color)
        self.dfs(image, sr, sc + 1, color)
        self.dfs(image, sr, sc - 1, color)
