class Solution:
    # TC --> O(N log N), SC --> O(N) using greedy approach
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        rec = nums[0]
        for num in nums:
            if num - rec > k:
                ans += 1
                rec = num
        return ans
