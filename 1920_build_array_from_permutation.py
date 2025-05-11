class Solution:
    # TC --> O(N), SC --> O(1)
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[nums[_]]for _ in range(n)]