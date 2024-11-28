class Solution:
    # Brute Force Approach TC --> O(N^2), SC --> O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if (nums[i]==nums[j]):
                    return True
        return False
    
    # Better Approach (By Sorting) TC --> O(N log N), SC -->O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if (nums[i]==nums[i-1]):
                return True
        return False
    
    # Optimal Approach (By creating Hashset) TC --> O(N), SC --> O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        