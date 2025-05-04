class Solution:
    # Brute force Approach
    # TC --> O(N^2), SC --> O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                length = j - i + 1
                score = curr_sum * length
                if score < k:
                    count += 1
                else:
                    break
                    # Since adding more elements will only increase sum and length,the score will increase. So we can break early.
        return count
    
    # Optimal approach
    # TC --> O(N), SC --> O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        curr_sum = 0
        count = 0
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            count += right - left + 1
        return count