class Solution:
    # TC --> O(log N), SC --> O(1) using binary search approach
    def first_occurrence(self, nums, target):
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first 

    def last_occurrence(self, nums, target):
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_occurrence(nums, target)
        if first == -1:
            return [-1,-1]
        last = self.last_occurrence(nums,target)
        return [first,last]