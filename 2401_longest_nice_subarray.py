class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # TC --> O(N), SC --> O(1)
        res = 0
        l = 0
        curr = 0  # bitmask
        for r in range(len(nums)):
            while curr & nums[r]:
                curr = curr ^ nums[l]
                l += 1
            res = max(res, r - l + 1)
            curr = curr | nums[r]
        return res
