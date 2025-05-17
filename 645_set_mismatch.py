class Solution:
    # Brute Force Approach
    # TC --> O(N^2), SC --> O(1)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, miss = -1, -1
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dup = i
            elif count == 0:
                miss = i
        return [dup, miss]
    
    # Better Approach 
    # TC --> O(N), SC --> O(N)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash = [0] * (n + 1)
        for num in nums:
            hash[num] += 1
        repeating = -1
        missing = -1
        for i in range(1, n + 1):
            if hash[i] == 2:
                repeating = i
            elif hash[i] == 0:
                missing = i
            if repeating != -1 and missing != -1:
                break
        return [repeating, missing]