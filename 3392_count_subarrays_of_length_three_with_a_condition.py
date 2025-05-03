class Solution:
    # TC --> O(N), SC --> O(1)
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(1, n - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                cnt += 1
        return cnt