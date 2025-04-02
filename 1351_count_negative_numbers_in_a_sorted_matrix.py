class Solution:
    # Brute Force approach
    # TC --> O(m*n), SC --> O(1)
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count
    
    # Optimal approach
    # TC --> O(log N), SC --> O(1)
    # Performing binary search for each row
    def binary_search(self, rows):  
        l, r = 0, len(rows)
        while l < r:
            mid = (l + r) // 2
            if rows[mid] < 0:
                r = mid
            else:
                l = mid + 1
        return len(rows) - l
    # Keep track of the Count by calling the above function
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for rows in grid:
            count += self.binary_search(rows)
        return count