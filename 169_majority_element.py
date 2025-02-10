class Solution:
    # Better approach
    # TC --> O(NxlogN) + O(N), SC --> O(N)
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mpp = {}
        for num in nums:
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1
            for num, count in mpp.items():
                if count > n//2:
                    return num
        return -1
    
    # Optimal approach using  Moore's Voting Algorithm
    # TC --> O(N) + O(N), SC --> O(1)
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        el = 0
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
            cnt1 = nums.count(el)
            if cnt1 > n // 2:
                return el
        return -1