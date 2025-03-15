class Solution:
    # TC -->O(N), SC --> O(1)
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
