class Solution:
    # TC-->O(N) using Kadane's algorithm, SC-->O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        maxi =  float('-inf')
        sum = 0
        start = 0
        ansStart = -1
        ansEnd = -1
        for i in range(len(nums)):
            if sum == 0:
                start = i 
            sum += nums[i]
            if sum > maxi:
                maxi = sum
                ansStart = start
                ansEnd = i 
            if sum < 0:
                sum = 0
        return maxi