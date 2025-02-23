class Solution:
    # Brute Force Approach 
    # TC --> O(N^2), SC --> O(1) 
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            curr_sum = 0
            for j in range(i,n):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1
        return count
    
    # Optimal Approach using hashmap
    # TC --> O(N), SC --> O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum_map = {0: 1}
        current_prefix_sum = 0
        subarray_count = 0
        for i in range(n):
            current_prefix_sum += nums[i]
            sum_to_remove = current_prefix_sum - k
            subarray_count += prefix_sum_map.get(sum_to_remove, 0)
            prefix_sum_map[current_prefix_sum] = (
                prefix_sum_map.get(current_prefix_sum, 0) + 1
            )
        return subarray_count
