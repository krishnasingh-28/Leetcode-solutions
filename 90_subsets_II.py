class Solution:
    # TC --> O(2^N*N), SC --> O(N)
    def func(self, ind, arr, nums, ans):
        if ind == len(nums):
            ans.append(arr.copy())
            return
        arr.append(nums[ind])
        self.func(ind + 1, arr, nums, ans)
        arr.pop()
        for j in range(ind + 1, len(nums)):
            if nums[j] != nums[ind]:
                self.func(j, arr, nums, ans)
                return
        self.func(len(nums), arr, nums, ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        nums.sort()
        self.func(0, arr, nums, ans)
        return ans
