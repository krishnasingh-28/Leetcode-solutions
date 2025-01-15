class Solution:
    # TC --> O(log N), SC --> O(1) using binary search approach
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:  # check if the left part is sorted
                if (
                    nums[low] <= target <= nums[mid]
                ):  # check if the target is between low & mid
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (
                    nums[mid] <= target <= nums[high]
                ):  # check if the target is between mid & high
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
