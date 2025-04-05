class Solution:
        # TC --> O(N), SC --> O(N)
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prefix_count = len(set(nums[: i + 1]))
            suffix_count = len(set(nums[i + 1 :]))
            res.append(prefix_count - suffix_count)
        return res
