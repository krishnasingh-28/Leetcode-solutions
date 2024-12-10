class Solution:
    # Brute force approach  TC --> O(2n), SC --> O(N)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len (nums)
        temp = [0]*n
        count = 0
        # copying the non zeros to the temp array
        for i in range(n):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1
        # copy the non zeros back to original array
        for i in range(count):
            nums[i] = temp[i]
        # filling the rest with zeros 
        for i in range(count, n):
            nums[i] = 0
        return nums
    
    # optimal approach (TC --> O(N), SC --> O(1))
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = -1
        # placing the pointer j
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1: # no non-zero elements
            return  
        # moving the pointers i,j and swapping it accordingly
        for i in range(j+1, n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums 