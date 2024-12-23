class Solution:
    # Brute force approach TC-->O(N^2), SC --> O(N^2)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n-1-i] = matrix[i][j]
        for i in range(n):
            matrix[i] = ans[i]

    # Optimal approach TC--> O(N^2), SC--> O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose of matrix
        for i in range(n):
            for j in range(i):
                # swap elements across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row of the matrix          
        for i in range(n):
            for j in range(n//2):
                # swap elements symmetrically
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    