class Solution:
    # Brute Force Approach TC --> O(N^2), SC -->O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n+1):
            flag = 0
            for num in nums:
                flag = 1
                break
            if flag == 0:
                return i
            
    # Better approach TC -->O(2N), SC -->O()
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * (n+1)
        for num in nums:
            freq[num] += 1
        for i in range(0, n+1):
            if freq[i] == 0:
                return i 
    
    # Optimal approach TC -->O(N), SC -->O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = (n*(n+1))//2
        sum2 = sum(nums)
        missing_number = sum1 - sum2
        return missing_number