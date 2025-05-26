class Solution:
    # TC --> O(N), SC --> O(1) using linear search 
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if (i == 0 or nums[i - 1] < nums[i]) and (
                i == n - 1 or nums[i] > nums[i + 1]
            ):
                return i
        return -1
    
    # TC --> O(log N), SC --> O(1) using binary search
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:  # left half
                high = mid - 1
            else:
                low = mid + 1
        return -1
