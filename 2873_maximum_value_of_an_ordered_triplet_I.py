class Solution:
    # TC --> O(N^2), SC --> O(1)
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = nums[0]
        for j in range(1, n):
            if nums[j] > left:
                left = nums[j]
            for k in range(j + 1, n):
                res = max(res, (left - nums[j]) * nums[k])
        return res
    