class Solution:
    # TC --> O(K*N), SC --> O(1)
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        return nums