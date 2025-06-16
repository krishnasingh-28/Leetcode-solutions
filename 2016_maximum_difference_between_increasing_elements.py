class Solution:
    # Brute Force Approach
    # TC --> O(N^2), SC --> O(1)
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    ans = max(ans, nums[j] - nums[i])
        return ans
    
    # Optimal Approach
    # TC --> O(N), SC --> O(1)
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                min_val = nums[i]
        return max_diff