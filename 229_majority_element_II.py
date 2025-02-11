class Solution:
    # Brute Force Approach
    # TC --> O(N^2), SC --> O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            if len(res) == 0 or res[0] != nums[i]:
                count = 0
                for j in range(n):
                    if nums[j] == nums[i]:
                        count += 1
                if count > (n//3):
                    res.append(nums[i])
            if len(res) == 2:
                break
        return res
    
    # Better Approach
    # TC --> O(N log N), SC --> O(N)
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        mpp = defaultdict(int)
        mini = (n // 3) + 1
        for num in nums:
            mpp[num] += 1
            if mpp[num] == mini:
                res.append(num)
            if len(res) == 2:
                break
        return res
    
    # Optimal Approach using Moore's Voting Algorithm
    # TC --> O(N) + O(N), SC --> O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1, cnt2 = 0, 0
        el1, el2 = float("-inf"), float("-inf")
        for num in nums:
            if cnt1 == 0 and el2 != num:
                cnt1 = 1
                el1 = num
            elif cnt2 == 0 and el1 != num:
                cnt2 = 1
                el2 = num
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            if num == el2:
                cnt2 += 1
        mini = n // 3 + 1
        result = []
        if cnt1 >= mini:
            result.append(el1)
        if cnt2 >= mini and el1 != el2:
            result.append(el2)
        return result