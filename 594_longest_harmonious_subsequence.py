class Solution:
    # using sorting approach
    # TC --> O(nlogn), SC --> O(1)
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        max_length = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                max_length = max(max_length, i - j + 1)
        return max_length   
    
    # using hashmap
    # TC --> O(N), SC --> O(N)
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_length = 0
        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])
        return max_length
