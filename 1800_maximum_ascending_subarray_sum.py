class Solution:
    # Brute Force Appproach 
    # TC --> O(N^2), SC --> O(1)
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        for i in range(len(nums)):
            curren_sum = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] > nums[j-1]:
                curren_sum += nums[j]
                j += 1
            max_sum = max(max_sum, curren_sum)
        return max_sum
    
    # Optimal Appproach 
    # TC --> O(N), SC --> O(1)
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curren_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                max_sum = max(max_sum, curren_sum)
                curren_sum = 0
            curren_sum += nums[i]
        return max(curren_sum,max_sum)