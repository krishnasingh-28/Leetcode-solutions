class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # FIXED LENGTH SLIDING WINDOW 
        # TC --> O(N), SC --> O(1)
        n = len(nums)
        curr_sum = 0 
        for i in range(k): # computing the k elements of the array
            curr_sum += nums[i] # summing up the first 4 contiguous elements
        max_avg = curr_sum / k # storing them into max_avg
        for i in range(k,n): # iterating the other part of the arr by leaving the first element
            curr_sum += nums[i] # summing up the other part
            curr_sum -= nums[i-k] # by leaving the before remaining part thus by sliding window 
            avg = curr_sum / k # avg of the other part 
            max_avg = max(max_avg, avg) # comparing and finding the maximum average value
        return max_avg 