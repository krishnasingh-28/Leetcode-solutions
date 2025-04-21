class Solution:
    # TC --> O(N), SC --> O(1)
    def minMoves(self, nums: List[int]) -> int:
        min_element = min(nums)
        summ = 0
        for num in nums:
            summ += num - min_element
        return summ
