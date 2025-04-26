class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # TC --> O(N^2), SC --> O(N)
        count = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            count += 1
        return count