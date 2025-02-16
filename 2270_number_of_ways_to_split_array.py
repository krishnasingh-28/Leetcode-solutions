class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # TC --> O(N), SC --> O(1)
        right = sum(nums)
        left = 0
        res = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                res += 1
        return res