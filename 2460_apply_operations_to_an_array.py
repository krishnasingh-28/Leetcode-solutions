class Solution:
    # TC --> O(N), SC --> O(1)
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0 
        l = 0 # left pointer
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return nums