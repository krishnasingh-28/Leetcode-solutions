class Solution:
    # TC --> O(N^2), SC --> O(1)
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        index = 0
        for i in range(len(nums)):
            flag = False
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    flag = True
                    break
            if not flag:
                res[index] = nums[i]
                index += 1
                if index == 2:
                    break
        return res
