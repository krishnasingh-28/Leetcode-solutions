class Solution:
    # TC --> O(N/2) using binary search approach, SC--> O(1)
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            # handle the duplicates 
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[low] <=  nums[mid]: # check if the left part is sorted
                if nums[low] <= target <= nums[mid]:#check if the target present on left half
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:#check if the target present on right half
                    low = mid + 1
                else:
                    high = mid - 1
        return False