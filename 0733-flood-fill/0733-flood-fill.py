class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]== color:
            return image

        def fill(image, sr, sc, color, oldcolor):
            if sr<0 or sc <0 or sr>= len(image) or sc >= len(image[0]) or image[sr][sc] != oldcolor:
                return
            image[sr][sc] = color
            fill(image, sr+1, sc, color, oldcolor)
            fill(image, sr-1, sc, color, oldcolor)
            fill(image, sr, sc+1, color, oldcolor)
            fill(image, sr, sc-1, color, oldcolor)
        
        fill(image, sr, sc, color, image[sr][sc])
        return image
        