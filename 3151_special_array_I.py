class Solution:
    # TC --> O(N), SC --> O(1)
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i] + nums[i - 1]) % 2 == 0:
                return False
        return True
