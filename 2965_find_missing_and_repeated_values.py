class Solution:
    # TC --> O(N^2), SC --> O(N^2) by using empty dictionary
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in count:
                    count[grid[i][j]] =0 
                count[grid[i][j]] += 1
                
        double, missing = 0, 0
        for num in range(1, n * n + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                double = num
        return [double, missing]


    # TC --> O(N^2), SC --> O(N^2) by using default dictionary which initializes value to 0 by default   
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        double, missing = 0, 0
        for num in range(1, n * n + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num
        return [double, missing]