class SEARCH2DMATRIX:
    """
    A class to represent a 2D matrix search.

    Attributes:
    matrix : List[List[int]]
        A 2D list of integers where the search will be performed.
    target : int
        The integer value to search for in the matrix.

    Methods:
    searchMatrix() -> bool:
        Searches for the target in the matrix and returns True if found, otherwise False.
    """

    def __init__(self, matrix, target):
        self.matrix = matrix
        self.target = target
    
    def searchMatrix(self) -> bool:
        if not self.matrix or not self.matrix[0]:
            return False
        
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = self.matrix[mid // cols][mid % cols]
            
            if mid_value == self.target:
                return True
            elif mid_value < self.target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False