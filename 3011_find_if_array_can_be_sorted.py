class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # TC --> O(N^2), SC--> O(N)
        n = len (nums)
        # Avoid modifying the input directly
        # Create a copy of the input array
        values = nums.copy()
        for i in range(n):
            for j in range(n-i-1):
                if values[j] <= values[j+1]:  # No swap needed
                    continue
                else:
                    if bin(values[j]).count("1") == bin(values[j+1]).count("1"):
                        values[j], values[j+1] = values[j+1], values[j] # Swap the elements
                    else:
                        return False
        return True
        