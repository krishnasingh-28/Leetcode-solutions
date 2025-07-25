class Solution:
    # TC --> O(N), SC --> O(N)
    def maxSum(self, nums: List[int]) -> int:
        n = set([num for num in nums if num > 0])
        return max(nums) if len(n) == 0 else sum(n)
