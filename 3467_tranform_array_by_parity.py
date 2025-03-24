class Solution:
    # TC --> O(N log N), SC --> O(N)
    def transformArray(self, nums: List[int]) -> List[int]:
        sorted_arr = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sorted_arr.append(0)
            else:
                sorted_arr.append(1)
        return sorted(sorted_arr)