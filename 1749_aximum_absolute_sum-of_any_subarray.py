class Solution:
    # Apporach 1 : Neetcode solution 
    # TC --> O(N), SC --> O(1)
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_prefix, min_prefix = 0, 0
        res = 0
        cur = 0
        for n in nums:
            cur += n
            res = max(res, abs(cur - max_prefix), abs(cur - min_prefix))
            min_prefix = min(cur, min_prefix)
            max_prefix = max(cur, max_prefix)
        return res
    
    # Approach 2 : leetcode editorial
    # TC --> O(N), SC --> O(1)
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        return max_prefix_sum - min_prefix_sum