class Solution:
    # Using Hash Map
    # TC --> O(N), SC --> O(N)
    def minOperations(self, nums: List[int], k: int) -> int:
        mpp = {}
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                mpp[i] = mpp.get(i, 0) + 1
        return len(mpp)
    
    # using Hash set
    # TC --> O(N), SC --> O(N)
    def minOperations(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        if mini < k:
            return -1
        st = set(nums)
        return len(st) - (mini == k)
