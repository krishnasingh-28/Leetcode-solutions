class Solution:
    # TC--> O(N), SC--> O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        max_count = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            elif nums[i] == 0:
                count = 0 
        return max_count