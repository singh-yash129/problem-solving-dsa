class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        # Create a prefix sum matrix with padding (extra row and column of 0s)
        # This simplifies the math and avoids "index out of bounds" checks
        self.pref = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                # Calculate prefix sum for the rectangle ending at (r, c)
                self.pref[r + 1][c + 1] = (matrix[r][c] + 
                                          self.pref[r][c + 1] + 
                                          self.pref[r + 1][c] - 
                                          self.pref[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Inclusion-Exclusion Principle in O(1)
        return (self.pref[row2 + 1][col2 + 1] - 
                self.pref[row1][col2 + 1] - 
                self.pref[row2 + 1][col1] + 
                self.pref[row1][col1])