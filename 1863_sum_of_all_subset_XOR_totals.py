class Solution:
    # TC --> O(N), SC --> O(1)
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num
        return result << (len(nums) - 1)
