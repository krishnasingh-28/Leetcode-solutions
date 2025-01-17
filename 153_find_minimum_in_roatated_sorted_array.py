class Solution:
    # TC -->O(log N) using binary search,SC-->O(1)
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        ans = float('inf')
        while low <= high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans