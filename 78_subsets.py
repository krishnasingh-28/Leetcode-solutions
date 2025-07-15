class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # TC --> O(2^N), SC --> O(N) + O(2^N * N)
        def backtrack(ind, path, ans):
            if len(nums) == ind:
                ans.append(path[:])
                return
            # Include nums[index]
            path.append(nums[ind])
            backtrack(ind + 1, path, ans)
            # Exclude nums[index]
            path.pop()
            backtrack(ind + 1, path, ans)
        ans = []
        backtrack(0, [], ans)
        return ans
