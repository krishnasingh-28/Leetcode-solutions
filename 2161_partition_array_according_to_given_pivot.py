class Solution:
    # dividing and appending approach
    # TC --> O(N), SC --> O(N)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        p = []
        greater = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                p.append(n)
        return less + p + greater
    
    # two pointers approach
    # TC --> O(N), SC --> O(N)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i2, j2 = 0, len(nums) - 1
        i, j = 0, len(nums) - 1
        res = [0] * len(nums)
        while i < len(nums):
            if nums[i] < pivot:
                res[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                res[j2] = nums[j]
                j2 -= 1
            i, j = i + 1, j - 1
        while i2 <= j2:
            res[i2] = res[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1
        return res