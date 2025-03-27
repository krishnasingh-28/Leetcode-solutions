class Solution:
    # TC --> O(1), SC --> O(1) Constant Time
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * (n * (n - 1) // 2)

    # TC --> O(1), SC --> O(1) using Gauss formula
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * (n * (n - 1) // 2)
    
    # TC --> O(N), SC --> O(1) LInear Time 
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(n):
            res += 4 * i
        return res