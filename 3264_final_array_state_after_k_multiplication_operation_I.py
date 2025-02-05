class Solution:
    
    # TC --> O(N*K), SC --> O(1)
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        return nums
        
    # TC --> O(N*K), SC --> O(1)
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for _ in range(k):
            min_index = 0
            for i in range(n):
                if nums[i] < nums[min_index]:
                    min_index = i
            nums[min_index] *= multiplier
        return nums