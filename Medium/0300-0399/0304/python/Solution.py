class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 < 0 or row2 > len(self.matrix) - 1 or col1 < 0 or col2 > len(self.matrix[0]) - 1:
            return None

        sum = 0
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                sum += self.matrix[row][col]

        return sum


# Your NumMatrix object will be instantiated and called as such:


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(1, 1, 2, 2))