class Solution:
    # TC --> O(log n), SC-->O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            m = l + ((r-l)//2)
            if ((m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m] != nums[m+1] )): #checking m neighbouring elements or if the desired element is present 1st or last 
                return nums[m]
            if nums[m-1] == nums[m]: # prefering leftside to check if it is same 
                leftsize = m-1
            else:
                leftsize = m 
            if leftsize % 2: # if the leftside of size is odd
                r = m - 1
            else:
                l = m + 1