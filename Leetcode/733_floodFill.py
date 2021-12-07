import collections


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        currColor = image[sr][sc]
        if currColor == newColor:
            return image
        n, m = len(image), len(image[0])
        queue = collections.deque([(sr, sc)])
        image[sr][sc] = newColor
        while queue:
            x, y = queue.popleft()
            for mx, my in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                    queue.append((mx, my))
                    image[mx][my] = newColor
        return image
