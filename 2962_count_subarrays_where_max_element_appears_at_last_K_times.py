class Solution:
    # Brute force approach
    # TC --> O(N^2), SC --> O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        count = 0
        for i in range(n):
            max_count = 0
            for j in range(i, n):
                if nums[j] == max_num:
                    max_count += 1
                if max_count >= k:
                    count += n - j  # all subarrays from i to j, j+1, ..., n-1 are valid
                    break  # no need to extend further, already ≥ k
        return count

    # Optimal Approach
    # TC --> O(N), SC --> O(1), using sliding window
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        max_nums = max(nums)
        max_count = 0
        l = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == max_nums:
                max_count += 1

            while max_count == k:
                if nums[l] == max_nums:
                    max_count -= 1
                l += 1
            res += l
        return res