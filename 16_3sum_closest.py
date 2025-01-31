class Solution:
    # Brute Force Approach
    # TC --> O(N^3), SC --> O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if abs (target-(nums[i]+nums[j]+nums[k]))< abs (target-closest):
                        closest = nums[i] + nums[j] + nums[k]
        return closest
    
    # TC --> O(N^2), SC -->O(N)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float("inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    lo += 1
                else:
                    hi -= 1
        return closest_sum