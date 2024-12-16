class Solution:
    # TC --> O(N+M), SC --> O(N+M)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        for num in set2:
            if num in set1:
                ans.append(num)
        return ans