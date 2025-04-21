class Solution:
    # TC --> O(N log N), SC --> O(1)
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        start, end = 0, len(nums) - 1
        while start < end:
            count += nums[end] - nums[start]
            start += 1
            end -= 1
        return count
