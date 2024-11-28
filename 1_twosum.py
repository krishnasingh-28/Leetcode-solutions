class Solution:
    # Brute Force Approach TC --> O(N^2), SC --> O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if (nums[i] + nums[j] == target):
                    return [i,j]
        return []        
    
    # Better approach: TC--> O(N), SC--> O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp ={}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            more_needed = target - num
            if more_needed in mpp:
                return [mpp[more_needed], i]
            mpp[num] = i
        return [-1, -1]
    
     # Optimal Approach :TC--> O(N)+O(N log N), SC --> O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]
        eleIndex = []
        for i in range(n):
            eleIndex.append([nums[i], i])
        eleIndex.sort(key = lambda x: x[0])
        left, right = 0, n - 1
        while left < right:
            sum_val = eleIndex[left][0] + eleIndex[right][0]
            if sum_val == target:
                ans[0] = eleIndex[left][1]
                ans[1] = eleIndex[right][1]
                return ans
            elif sum_val < target:
                left += 1
            else:
                right -= 1 
        return ans